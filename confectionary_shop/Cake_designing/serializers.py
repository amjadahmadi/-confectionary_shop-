from rest_framework import serializers
from .models import Feeling, Taste


class FeelingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Feeling
        fields = '__all__'


class TasteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Taste
        fields = '__all__'
