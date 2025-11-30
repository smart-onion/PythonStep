from django.contrib import admin

# Register your models here.
from .models import *

# admin.site.register(Film)
# admin.site.register(Comment)


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "comments_quantity")
    list_filter = ("rating", )

    def comments_quantity(self, o: Film):
        return o.comment_set.count()

    def some_info(self, obj: Film):
        return obj.name
    

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "text", "date")

    list_filter = ("date", )

    def has_change_permission(self, request, obj = ...):
        return request.user.has_perm("app.can_moderate_comments") 
    def has_delete_permission(self, request, obj = ...):
        return request.user.has_perm("app.can_moderate_comments")
    
    
@admin.register(Ganre)
class GanreAdmin(admin.ModelAdmin):
    list_display = ("name", )