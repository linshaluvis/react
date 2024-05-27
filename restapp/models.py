from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    pass

class restapi(models.Model):
    name = models.CharField(max_length=200,null=True)
    age = models.CharField(max_length=200,null=True)
    course = models.CharField(max_length=200,null=True)
