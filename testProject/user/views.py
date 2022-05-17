from rest_framework import generics
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth import get_user_model
from django.db.models.query import QuerySet
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from user.filters import UserFilters
from user.serializers import UserSerializer, LimitedUserSerializer, LimitedUserSerializerInfo

User = get_user_model()


class UserListWithIDAndUsername(generics.ListAPIView):
    queryset = User.objects.all().order_by('-total_toll_paid')
    serializer_class = LimitedUserSerializer


class UserListWithIDAndUsernameInfo(generics.ListAPIView):
    queryset = User.objects.all().order_by('-total_toll_paid')
    serializer_class = LimitedUserSerializerInfo


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_class = UserFilters
    filter_backends = [DjangoFilterBackend]

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = UserSerializer(
            queryset, many=True, context={'request': request})
        return Response(serializer.data)

    # def get_queryset(self):
    #     q: QuerySet = self.queryset.all()
    #     qp = self.request.query_params
    #     req_color = qp.get('color')
    #     req_age = qp.get('owner_age')
    #     req_length = qp.get('length')
    #     req_question_4 = json.loads(qp.get('question_4','False'))
    #     req_type = qp.get('type')
    #     if req_type:
    #         q = q.filter(type__iexact=req_type)

    #     if req_length:
    #         q = q.filter(length__gte=float(req_length))

    #     if req_color:
    #         req_color = req_color.split(',')
    #         if isinstance(req_color, (list, tuple, set)):
    #             q = q.filter(color__in=req_color)
    #     if req_age:
    #         q = q.filter(Owner__age__gte=int(req_age))
    #     if req_question_4:
    #         q = \
    #             (q
    #              .filter(roads_traveled__width__gte=RoadRules.BigCarMaxRoadWidth.value)
    #              .filter(type__exact=CarType.Big.value)
    #             )
    #     return q
