from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    username = models.EmailField(unique=True)
    email = models.EmailField(unique=True)