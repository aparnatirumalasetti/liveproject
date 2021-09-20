from django.db import models
from django.utils import timezone
class school(models.Model):
    Std_name=models.CharField(max_length=100)
    #Std_roll=models.IntegerField(validators=[validate_price])
    Email=models.EmailField(default="@gmail.com")
    standard=models.CharField(max_length=100)
    Address=models.CharField(max_length=100)
    mobile=models.BigIntegerField(null=True)
# Create your models here.
