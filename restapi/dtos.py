from rest_framework import serializers


class ValidateDriverAddParams(serializers.Serializer):
    name = serializers.CharField(max_length=30)
    email = serializers.EmailField(max_length=100)
    phone_number = serializers.CharField(min_length=10, max_length=10)
    license_number = serializers.CharField(max_length=20)
    car_number = serializers.CharField(max_length=15)


class ValidateDriverLocationParams(serializers.Serializer):
    latitude = serializers.FloatField(required=True)
    longitude = serializers.FloatField(required=True)
