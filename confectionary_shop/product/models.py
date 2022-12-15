from datetime import datetime

from django.core.validators import RegexValidator
from django.db import models
from django.http import JsonResponse

from .managers import StockManagers
from Cake_designing.models import Cake_Designing
from customer.models import User
from core.models import BaseModel
from django.db.models import Q

# Create your models here.


class Discount_Code(BaseModel):
    discount_name = models.CharField(max_length=100)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    amount = models.FloatField()
    percent = models.BooleanField()


class Products(BaseModel):
    product_name = models.CharField(max_length=100)
    img = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return f"{self.product_name}({self.description})"


class Category(BaseModel):
    category_name = models.CharField(max_length=100)
    img = models.ImageField(default='draw1.png', null=True, blank=True)
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.category_name


class Discount(BaseModel):
    product = models.OneToOneField("Stock", on_delete=models.CASCADE, null=True, blank=True, related_name='dis')
    # category_id = models.OneToOneField(Category, on_delete=models.CASCADE, null=True, blank=True)
    cake_designing_id = models.OneToOneField(Cake_Designing, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.FloatField()
    percent = models.BooleanField()
    active = models.BooleanField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    # class Meta:
    #     ordering = 'id'

class Stock(BaseModel):
    product = models.OneToOneField(Products, on_delete=models.CASCADE)
    kilo = models.FloatField(null=True, blank=True)
    count = models.IntegerField(null=True, blank=True)
    price = models.FloatField()
    after_discount = models.FloatField(null=True, blank=True)
    category = models.ManyToManyField(Category)
    stock_manager = StockManagers()

    def __str__(self):
        return self.product.product_name

    def _after_discount(self, amount, percent):
        if percent:
            return self.price * (1 - (amount / 100))

        return self.price - amount

    def get_product(self):
        queryset = Discount.objects.filter(product=self).values().last()
        if queryset:
            return queryset
        return None