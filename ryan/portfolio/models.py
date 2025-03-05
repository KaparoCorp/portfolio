from django.db import models

# Create your models here.
class Contact_info(models.Model):
    first_name = models.CharField(max_length=50,blank=False, name='first_name')
    second_name = models.CharField(max_length=50, blank=False, name='second_name')
    email = models.EmailField(blank=False,unique=True, name='email')
    message = models.CharField(max_length=1000, blank=False ,name='message')