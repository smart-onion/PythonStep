from django.urls import path
from . import views
urlpatterns = [
    path("register", views.register_view, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("comment_create/<int:id>", views.comment_create, name="comment_create"),
    path("comment_delete/<int:id>", views.comment_delete, name="comment_delete"),
    path("comment_like", views.comment_like, name="comment_like"),
    path("discussion/<int:id>", views.discussion_view, name="discussion"),
    path("discussions/<int:id>", views.discussions_view, name="discussions"),
    path("discussion_like", views.discussion_like, name="discussion_like"),
    path("discussion_create", views.discussion_create_view, name="discussion_create"),
    path("discussion_update/<str:id>", views.discussion_edit_view, name="discussion_update"),
    path("discussion_delete/<str:id>", views.discussion_delete_view, name="discussion_delete"),

    path('favorites', views.favorites_view, name='favorites'),

    path("", views.categories_view, name="categories",),
    path("author/<int:author_id>", views.author_view, name="author",)
]