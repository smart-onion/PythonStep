from django.urls import path
from task import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add', views.add_task, name="add_task"),
    path('remove/<int:id>', views.remove_task, name="remove_task"),
]