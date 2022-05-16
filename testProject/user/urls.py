from django.urls import path

from user.views import UserList

urlpatterns = [

    path('list/',UserList.as_view())

]