from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    image = models.ImageField(upload_to='avatars', null=True, blank=True)
    
class Post(models.Model):
    name = models.CharField(max_length=50)