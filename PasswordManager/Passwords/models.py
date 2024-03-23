from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PasswordBlock(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    platform = models.CharField(max_length = 200)
    username = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)