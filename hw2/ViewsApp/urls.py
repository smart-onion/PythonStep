from django.urls import path
from ViewsApp import views

urlpatterns = [
    path('json/', views.JsonNormalizer.as_view()),
    path('mobile-page', views.mobile_page, name="mobile-page"),
    path("agent", views.CheckUserAgent.as_view()),
    path('data/<str:key>', views.get_data, name="get-data"),
    path('update-data', views.post_data, name="update-data"),
]