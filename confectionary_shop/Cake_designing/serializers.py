from rest_framework import serializers
from .models import Feeling, Taste, Cake_Designing


class FeelingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Feeling
        fields = '__all__'


class TasteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Taste
        fields = '__all__'


class CakeDesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cake_Designing
        fields = '__all__'
