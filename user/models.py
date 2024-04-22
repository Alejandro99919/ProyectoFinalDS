from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
	picture = models.ImageField(default='profile_default.png', upload_to='users/')
	location = models.CharField(max_length=60, null=True, blank=True)
	bio = models.TextField(max_length=400, null=True, blank=True)