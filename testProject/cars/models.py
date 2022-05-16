from django.contrib.gis.db import models

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
    load_valume = models.FloatField(null=True)
    
    def __str__(self) -> str:
        return f'{self.id} - {self.type} - {self.color}' 

__all__ = ["Car", "CarType", "Color"]