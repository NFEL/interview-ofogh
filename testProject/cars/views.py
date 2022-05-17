import json
from typing import Iterable, List
from django.http import HttpRequest, JsonResponse
from cars.models import Car,CarType
from rest_framework import generics
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import get_user_model
from django.db.models.query import QuerySet
from django.contrib.gis.measure import Distance
from cars.serializers import CarSerializer
from cars.filters import CarFilters
from road.Utils.geom_zones import TEHRAN_GEOM, TOLL_1
from road.regulations import RoadRules

User = get_user_model()


def _color_filter(colors: Iterable[str]) -> List[dict]:
    return list(Car.objects.filter(color__in=colors).values() or [])


def _owner_age_filter(age: int) -> List[dict]:
    return list({_.get('cars') for _ in User.objects.filter(age__gte=age).prefetch_related('cars').values('cars')})


# Manual QueryParsing
# Sample Query http://localhost:8000/car/listMethod/?color=%22black%22,%22white%22
# Sample Query http://localhost:8000/car/listMethod/?color=%22red%22,%22blue%22
# SQ http://localhost:8000/car/listMethod/?age=20
# SQ http://localhost:8000/car/listMethod/?age=70
def get_car_with_filter(req: HttpRequest) -> JsonResponse:
    if req.method == 'GET':
        req_color = req.GET.get('color')
        req_age = req.GET.get('age')
        if req_color is not None:
            req_color = eval(req_color)
            if not isinstance(req_color, (list, tuple, set)):
                req_color = (req_color,)
            return JsonResponse({"cars": _color_filter(req_color)})
        elif req_age is not None:
            return JsonResponse({"cars": _owner_age_filter(eval(req_age))})

        else:
            return JsonResponse({"cars": list(Car.objects.all().values())})


class CarList(generics.ListCreateAPIView):
    filter_class = CarFilters
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [DjangoFilterBackend]

    def list(self, request):
        queryset = self.get_queryset()
        serializer = CarSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def get_queryset(self):
        q: QuerySet = self.queryset.all()
        qp = self.request.query_params
        req_color = qp.get('color')
        req_age = qp.get('owner_age')
        req_length = qp.get('length')
        req_question_4 = json.loads(qp.get('question_4','False'))
        req_question_6 = json.loads(qp.get('question_6','False'))
        req_type = qp.get('type')
        if req_type:
            q = q.filter(type__iexact=req_type)
            
        if req_length:
            q = q.filter(length__gte=float(req_length))
            
        if req_color:
            req_color = req_color.split(',')
            if isinstance(req_color, (list, tuple, set)):
                q = q.filter(color__in=req_color)
        if req_age:
            q = q.filter(Owner__age__gte=int(req_age))
        if req_question_4:
            q = \
                (
                    q
                    .filter(roads_traveled__width__gte=RoadRules.BigCarMaxRoadWidth.value)
                    .filter(type__exact=CarType.Big.value)
                )
        if req_question_6:
            q =\
                (
                    q
                    .filter(current_location__distance_lte = (TOLL_1,Distance(m=600)))
                    .filter(current_location__dwithin = (TEHRAN_GEOM,Distance(m=600)))
                    .filter(type__exact=CarType.Small.value)
                )
        return q
