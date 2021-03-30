from rest_framework import serializers


class DriverSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=30)
    email = serializers.CharField(max_length=100)
    phone_number = serializers.CharField(max_length=10)
    license_number = serializers.CharField(max_length=20)
    car_number = serializers.CharField(max_length=15)


class NearByDriverSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    car_number = serializers.CharField(max_length=15)
    phone_number = serializers.CharField(max_length=10)
