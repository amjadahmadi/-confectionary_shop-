from datetime import datetime

from django.db import models


class StockManagers(models.Manager):
    def get_queryset(self):
        # products = super().get_queryset().all().select_related('dis')
        # [i._after_discount(i.dis.amount, i.dis.percent) for i in products]
        return super().get_queryset().filter(is_deleted=False).select_related('dis')


class DiscountCodeManagers(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(start_date__lt=datetime.now(), end_date__gt=datetime.now())
