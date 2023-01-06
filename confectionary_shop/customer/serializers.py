from rest_framework import serializers
from .models import Addresses, Profile, User


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addresses
        fields = '__all__'
        read_only_fields = ('user',)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
