from django.db import models

# Create your models here.
class Login_model(models.Model):
    Name = models.CharField(max_length=50)
