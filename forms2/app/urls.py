from django.urls import path
from . import views
urlpatterns = [
    path('add_film', views.get_add_film, name="add_film"),
    path('post_film', views.post_add_film, name="post_film"),
    path('film/<str:id>', views.show_film, name="film"),
    path('', views.index, name="index"),
    path('delete_film', views.delete_film, name="delete_film"),
    path("create-ganre", views.get_create_ganre, name="create_ganre"),
    path("post-ganre", views.post_create_ganre, name="post_ganre"),
    path("all-ganres", views.get_all_ganres, name="all_ganres"),
    path("post-comment", views.post_create_comment, name="post_comment"),
    path("delete-comment/<int:comment_id>", views.delete_comment, name="delete_comment")
]

