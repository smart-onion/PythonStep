from django.urls import path
from news import views
urlpatterns = [
    path('', views.index, name="news_index"),
    path("<str:category>", views.category_page, name="category_page"),
    path("<str:category>/<str:id>", views.curr_news, name="curr_news")
]
