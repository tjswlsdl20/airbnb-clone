from django.contrib import admin
from . import models


@admin.register(models.Room)
class roomAdmin(admin.ModelAdmin):
    pass


# Register your models here.
