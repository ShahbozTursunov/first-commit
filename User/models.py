from django.db import models
from django.core.validators import RegexValidator
from rest_framework.validators import ValidationError

# Create your models here.
class Register(models.Model):
    phone_regex = [RegexValidator(regex="d{0,9}", message="Iltimos davom eting: +998XXXXXXXXX"),]
    phone = models.CharField(max_length=20, validators=phone_regex, unique=True)
    ism = models.CharField(max_length=255)
    password = models.CharField(max_length=8)
    familiya = models.CharField(max_length=255)
    nick = models.CharField(max_length=255)
    card = models.CharField(max_length=16)
    
    def __str__(self) -> str:
        return self.ism

class Order(models.Model):
    narx = models.CharField(max_length=255)
    pay = (
        ("Oziq-ovqat", "Oziq-ovqat"),
        ("kommunal", "kommunal"),
        ("mobil-operator", "mobil-operator"),
        ("internet", "internet"),
        ("yo'l haqqi", "yo'l haqqi"),
        ("pul o'tkazmalari", "pul o'tkazmalari"),
        ("boshqa", "boshqa")
    )
    category = models.CharField(max_length=255, choices=pay)
    sana = models.DateTimeField(auto_now=True)
    card = models.ForeignKey(Register, on_delete=models.CASCADE)

    def __str__(self):
        return self.category