from django.http.response import HttpResponse
from django.views.generic import CreateView
from .serializers import UserSerializer


from django.contrib.auth import get_user_model

User = get_user_model()

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAdminUser]

    def list(self, request):
        # Note the use of `get_queryset()` instead of `self.queryset`
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True,context={'request': request})
        return Response(serializer.data)