from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialty= models.CharField(max_length=255, default="Default specialty")
    first_name= models.CharField(max_length=255, default="Employee First Name")
    last_name= models.CharField(max_length=255, default="Employee Last Name")
