from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class CustomUser(AbstractUser):
    region = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)

    def __str__(self):
        return self.username


class GoldUser(models.Model):
    validate_date = models.DateField()

    class Meta:
        permissions = [('gold_member', 'Gold member')]

