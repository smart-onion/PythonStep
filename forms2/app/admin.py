from django.contrib import admin

# Register your models here.
from .models import *

# admin.site.register(Film)

@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ("id", "name")