from django.db import models


# Create your models here.

class BaseModel(models.Model):
    is_deleted = models.BooleanField(default=False)
