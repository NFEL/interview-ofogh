from django.urls import path

from user.views import UserList, UserListWithIDAndUsername,UserListWithIDAndUsernameInfo

urlpatterns = [

    path('list/sorted/info',UserListWithIDAndUsernameInfo.as_view()),
    path('list/sorted/',UserListWithIDAndUsername.as_view()),
    path('list/',UserList.as_view()),

]