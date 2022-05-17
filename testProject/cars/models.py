from typing import Optional,Iterable
from django.utils import timezone
from django.contrib.gis.db import models

from road.models import Road

class CarType(models.Choices):
    Small = "small"
    Big = "big"

class Color(models.Model):
    name = models.CharField("Color-Name",max_length=255)
    def __str__(self) -> str:
        return f'{self.name}'

class Car(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(choices=[(CarType.Small.value,CarType.Small.value),(CarType.Big.value,CarType.Big.value),],max_length=150)
    color = models.CharField(max_length=255)
    length = models.FloatField()
    current_location = models.PointField("Current location of the car",auto_created=True,null=True)
    last_update_location = models.DateTimeField(null=True)
    load_valume = models.FloatField(null=True)
    roads_traveled = models.ManyToManyField(
        Road,
        through='Travel',
        related_query_name='RoadTravel',
        related_name='Traveled'
    ) 
    
    def save(self,
             *args, update_fields: Optional[Iterable[str]] = ...,**kwargs,) -> None:
        if 'current_location' in update_fields:
            self.current_location = timezone.now()
        return super().save(*args,**kwargs, update_fields=update_fields)
    
    def __str__(self) -> str:
        return f'{self.id} - {self.type} - {self.color}' 



class Travel(models.Model):
    car = models.ForeignKey(Car,on_delete=models.CASCADE)
    road = models.ForeignKey(Road,on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name="Time Of passage", auto_now_add=True)


__all__ = ["Car", "CarType", "Color"]