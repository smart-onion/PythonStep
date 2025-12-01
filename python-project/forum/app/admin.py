from django.contrib import admin
from .models import *
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")

@admin.register(Discussion)
class DiscussionAdmin(admin.ModelAdmin):
    list_display = ("id", "subject", "author", "issued")

@admin.register(Comment)
class DiscussionAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "issued")