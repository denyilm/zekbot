from django.db import models

from django.db.models import constraints
from django.db.models.fields import FloatField, IPAddressField
from django.contrib.postgres.fields import ArrayField
from django.forms import ModelForm, Textarea
from django.utils.crypto import get_random_string

# Create your models here.

class Eth(models.Model):
    id=models.AutoField(primary_key=True, editable = False)
    pair=models.CharField(blank=True, null=True, max_length=20)
    price=models.FloatField(blank=True, null=True)
    date=models.DateTimeField(auto_now=True)


class Shib(models.Model):
    id=models.AutoField(primary_key=True, editable = False)
    pair=models.CharField(blank=True, null=True, max_length=20)
    price=models.FloatField(blank=True, null=True)
    date=models.DateTimeField(auto_now=True)