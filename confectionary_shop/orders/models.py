import datetime

from django.core.validators import RegexValidator
from django.db import models
from core.models import BaseModel
from customer.models import User
from .validators import test
from product.models import Discount_Code


# Create your models here.

class Orders(BaseModel):
    class Payment_Status(models.TextChoices):
        pre_payment = "PR", "Pre Payment"
        payed = "PY", "Payed"

    date = models.DateTimeField(auto_now_add=True)
    total_price = models.FloatField()
    final_price = models.FloatField()
    discount_code_id = models.ForeignKey(to='product.Discount_Code', on_delete=models.CASCADE, null=True, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField()
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, validators=[test], null=True, blank=True)
    payment_status = models.CharField(max_length=2, choices=Payment_Status.choices, default=Payment_Status.pre_payment)

    @staticmethod
    def valid_discount_code(discount_id):
        try:
            Discount_Code.active_manger.get(id=discount_id)
            return True
        except Discount_Code.DoesNotExist:
            return False


class Order_Item(BaseModel):
    class Order_Status(models.TextChoices):
        canceled = "CA", "Canceled"
        submitted = "SU", "Submitted"

    order_id = models.ForeignKey(Orders, on_delete=models.CASCADE)
    stock_id = models.ForeignKey(to='product.Stock', on_delete=models.CASCADE)
    amount = models.FloatField()
    kilo = models.BooleanField()
    price = models.FloatField()
    after_discount = models.FloatField(null=True, blank=True)
    total_price = models.FloatField()
    discount_id = models.ForeignKey(to='product.Discount', on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    pre_order = models.BooleanField()
    ready_time = models.DateTimeField(null=True, blank=True)
    order_status = models.CharField(max_length=2, choices=Order_Status.choices, default=Order_Status.submitted)
