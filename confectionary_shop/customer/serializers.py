from rest_framework import serializers
from .models import Addresses, Profile, User, Bank_Account


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addresses
        # fields = '__all__'
        read_only_fields = ('user',)
        exclude = ('is_deleted', 'create_at', 'update_at')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        # fields = '__all__'
        exclude = ('is_deleted', 'create_at', 'update_at')


class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bank_Account
        # fields = '__all__'
        exclude = ('is_deleted', 'create_at', 'update_at')


class UserSerializer(serializers.ModelSerializer):
    bank_account = BankSerializer()
    profile = ProfileSerializer()
    addresses = serializers.SerializerMethodField()

    class Meta:
        model = User
        # fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True}
        }
        exclude = ('is_superuser', 'is_staff', 'last_login', 'is_active', 'date_joined', 'groups',
                   'user_permissions')

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def update(self, instance, validated_data):

        password = validated_data.pop('password', None)

        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        instance.save()

        return instance

    def get_addresses(self, obj:User):
        return AddressSerializer(obj.user_address(),many=True).data


