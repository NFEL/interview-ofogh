from django.contrib.gis.db import models

from cars.models import Car

class TollStation(models.Model):
    name= models.CharField(max_length=255)
    toll_per_cross=models.IntegerField("Toll Price per car cross")
    location = models.PointField(primary_key=True,srid=4326)
    
    def __str__(self) -> str:
        return f'{self.name} - {self.location} - {self.toll_per_cross} '
    
class Road(models.Model):
    # There Was Null row in given data
    name = models.CharField(max_length=255, null=True)
    width = models.FloatField("Road Length")
    geom = models.MultiLineStringField(srid=4326)
    
    def __str__(self) -> str:
        return f'{self.name} - {self.geom}'
    
class Travel(models.Model):
    car = models.ForeignKey(Car,on_delete=models.CASCADE)
    road = models.ForeignKey(Road,on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name="Time Of passage", auto_now_add=True)

__all__ = ["Travel", "Road", "TollStation"]
