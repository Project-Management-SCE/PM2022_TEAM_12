from django.db import models
from django.contrib.auth.models import AbstractUser
#from django.utils.html import escape, make_safe
# Create your models here.

class User(AbstractUser):
    is_passenger=models.BooleanField(default=False)
    is_Admin=models.BooleanField(default=False)
class Driver(User):
    companyName=models.CharField(max_length=100,default='')
    phone=models.CharField(max_length=10,default='')
    is_ok= models.BooleanField(default=False)
    License=models.FileField(upload_to='files/', null=True)
    certificate=models.FileField(default=None)

    class Meta:
        db_table = 'Drivers'

class Updates(models.Model):
    senderID=models.CharField(max_length=100,default='')
    message=models.CharField(max_length=10,default='')

    class Meta:
        db_table = 'Updates'
    
