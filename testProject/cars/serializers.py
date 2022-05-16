from rest_framework import serializers
from cars.models import Car,CarType

class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = '__all__'
        read_only_fields = ['id',]


    def create(self, validated_data):
        obj, _ = Car.objects.update_or_create(**validated_data)
        return obj
