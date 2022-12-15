from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.core.validators import RegexValidator
from core.models import BaseModel


class CustomManager(BaseUserManager):
    def create_user(self, phone, password, **kwargs):
        user = self.model(phone=phone, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, phone, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)
        return self.create_user(phone, password, **kwargs)


# Create your models here.
class Bank_Account(BaseModel):
    balance = models.FloatField(default=0)
    card_bank = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.card_bank


class Profile(BaseModel):
    class Gender(models.TextChoices):
        male = "MA", "Male"
        female = "FE", "Female"

    email = models.EmailField(null=True)
    gender = models.CharField(max_length=2, choices=Gender.choices, default=Gender.male)
    birth_day = models.DateTimeField(null=True)

    def __str__(self):
        return self.email


class User(AbstractUser, PermissionsMixin):
    username = None
    email = None
    phone = models.CharField(max_length=50, unique=True, validators=[RegexValidator(r'^(\+98|0)\d{10}')])
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, null=True)
    bank_account = models.OneToOneField(Bank_Account, on_delete=models.CASCADE, null=True)
    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []
    objects = CustomManager()

    def __str__(self):
        return self.phone


class Addresses(BaseModel):
    full_address = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    stock_id = models.ForeignKey('product.Stock', on_delete=models.CASCADE)
    comment_body = models.TextField()
    rate = models.FloatField()
