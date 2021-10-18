from django.contrib import admin
from register.models import Register_model

# Register your models here.
admin.site.register(Register_model)


def __str__(self):
    return self.name