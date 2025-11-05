from django.shortcuts import render
from datetime import datetime, timedelta


tasks = [
    {"title": "Task one", "category": "one", "time": datetime.now() + timedelta(days=5), "completed": True},
    {"title": "Task two", "category": "two", "time": datetime.now() + timedelta(days=2), "completed": False},
    {"title": "Task three", "category": "three", "time": datetime.now() + timedelta(days=6), "completed": True},
    {"title": "Task F", "category": "three", "time": datetime.now() + timedelta(days=6), "completed": False},
]

context = {
    "tasks": tasks
}

def index(req):
    return render(req, "index.html", context=context)