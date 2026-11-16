from rest_framework import serializers
from turf_management.models import Turf

class TurfSerializers(serializers.Serializer):

    id = serializers.IntegerField()

    name = serializers.CharField()

    location = serializers.CharField()

    address = serializers.CharField()

    description = serializers.CharField()

    opening_time = serializers.TimeField()

    closing_time = serializers.TimeField()

    day_price = serializers.DecimalField(max_digits=10,decimal_places=2)

    night_price = serializers.DecimalField(max_digits=10,decimal_places=2)

    facilities = serializers.CharField()

    def create(self, validated_data):
        return Turf.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        for attribute,value in validated_data.items():
            setattr(instance,attribute,value)

        return instance