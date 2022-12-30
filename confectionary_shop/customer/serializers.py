from rest_framework import serializers
from .models import Addresses


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addresses
        fields = '__all__'
