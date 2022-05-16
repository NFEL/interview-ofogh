from django.urls import path
from cars.views import get_car_with_filter,CarList

urlpatterns = [

    path('list/',get_car_with_filter),
    path('listView/',CarList.as_view())

]