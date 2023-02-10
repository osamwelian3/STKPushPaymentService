from django.db import models
from django.core.validators import RegexValidator
import datetime

# Create your models here.
class Payment(models.Model):
    transaction_id = models.CharField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=20)
    amount = models.FloatField()
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Payment {self.transaction_id}"

class Token(models.Model):
    access_token = models.CharField(max_length=255, unique=True)
    expiry = models.DateTimeField(default=datetime.datetime.now()+datetime.timedelta(0,3599))

    def __str__(self) -> str:
        return f"Access token: {self.access_token}"
