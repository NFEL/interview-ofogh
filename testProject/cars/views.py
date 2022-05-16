from typing import Iterable, List
from django.http import HttpRequest, JsonResponse
from cars.models import Car
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from cars.serializers import CarSerializer


User = get_user_model()


def _color_filter(colors: Iterable[str]) -> List[dict]:
    return list(Car.objects.filter(color__in=colors).values() or [])

def _owner_age_filter(age:int) -> List[dict]:
    return list({_.get('cars') for _ in User.objects.filter(age__gte=age).prefetch_related('cars').values('cars')})


# Sample Query http://localhost:8000/car/list/?color=%22black%22,%22white%22
# Sample Query http://localhost:8000/car/list/?color=%22red%22,%22blue%22
# SQ http://localhost:8000/car/list/?age=20
# SQ http://localhost:8000/car/list/?age=70
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
            return JsonResponse({"cars":list(Car.objects.all().values())})


class CarList(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    # permission_classes = [IsAdminUser]

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = CarSerializer(queryset, many=True,context={'request': request})

        return Response(serializer.data)
    