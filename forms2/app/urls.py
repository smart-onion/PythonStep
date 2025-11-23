from django.urls import path
from . import views
urlpatterns = [
    path('add_film', views.get_add_film, name="add_film"),
    path('post_film', views.post_add_film, name="post_film"),
    path('film/<str:id>', views.show_film, name="film"),
    path('', views.index, name="index"),
    path('delete_film', views.delete_film, name="delete_film"),
]

