from django.contrib import admin
from login.models import Login_model

#Register your models here.
admin.site.register(Login_model)

def __str__(self):
    return self.name