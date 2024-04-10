from rest_framework import serializers
from .models import City,Person,PersonAddress,Interest


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model=City
        fields=['title']

class InterestSerializer(serializers.ModelSerializer):
   
    class Meta:
        model=Interest
        fields="__all__"

class PersonSerializer(serializers.ModelSerializer):  

    class Meta:
        model=Person
        fields = '__all__'

class PersonAddressSerializer(serializers.ModelSerializer):
    city = serializers.CharField(source="city.title")
   
    class Meta:
        model=PersonAddress
        fields='__all__'   

