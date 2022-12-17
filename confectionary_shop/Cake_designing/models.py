from django.db import models
from core.models import BaseModel
import orders.models as e


# Create your models here.

class Feeling(BaseModel):
    feeling_name = models.CharField(max_length=100)
    price = models.FloatField()


class Taste(BaseModel):
    Taste_name = models.CharField(max_length=100)
    price = models.FloatField()


class Cake_Designing(BaseModel):
    class Payment_Status(models.TextChoices):
        pre_payment = "PR", "Pre Payment"
        payed = "PY", "Payed"

    amount = models.FloatField()
    price = models.FloatField()
    sample_img = models.ImageField(null=True, blank=True)
    print_img = models.ImageField(null=True, blank=True)
    ready_time = models.DateTimeField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    payment_status = models.CharField(max_length=2, choices=Payment_Status.choices, default=Payment_Status.pre_payment)
    extra_payment = models.FloatField(null=True, blank=True)
    feeling_id = models.ForeignKey(Feeling, on_delete=models.CASCADE)
    taste_id = models.ForeignKey(Taste, on_delete=models.CASCADE)
    order_id = models.ForeignKey(e.Orders, on_delete=models.CASCADE)
