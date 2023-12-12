from django.db import models
from django.conf import settings
# Create your models here.
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    first_name = None
    last_name = None
    age = models.IntegerField(default=0)