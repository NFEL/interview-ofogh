from django.urls import path
from cars.views import get_car_with_filter,CarList

urlpatterns = [

    path('list/',CarList.as_view()),
    path('listMethod/',get_car_with_filter),

]