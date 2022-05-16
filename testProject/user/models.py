from django.contrib.auth.models import AbstractUser
from django.contrib.gis.db import models
from cars.models import Car

class User(AbstractUser):
    national_code = models.CharField("User National ID",max_length=20, primary_key=True)
    # name = models.CharField(max_length=255) # Username already exists
    age= models.IntegerField("User Age")
    total_toll_paid= models.IntegerField("User National ID", default=0)
    cars = models.ManyToManyField(Car,related_name="Owns",related_query_name="Owner")

    REQUIRED_FIELDS = ['national_code','age']

    def __str__(self) -> str:
        # print()
        return f'{self.username} - {self.national_code}'
    