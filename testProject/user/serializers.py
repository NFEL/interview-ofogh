from rest_framework import serializers


from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    # cars = serializers.ManyRelatedField(many=True, read_only=True,child_relation=)
    

    class Meta:
        model = User
        # fields = '__all__'
        fields = ['username','national_code', 'email','age' ,'password','cars']
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ['total_toll_paid',]
        # lookup_field = 'username'

    def create(self, validated_data):
        cars = validated_data.pop('cars')
        # password = validated_data.pop('password')
        user = User.objects.create_user(
            **validated_data
        )
        # user.set_password(password)
        user.cars.set([car.id for car in cars])
        user.save()
        return user

