from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="form_index"),
    path('events', views.post_event, name="events_p")
]
