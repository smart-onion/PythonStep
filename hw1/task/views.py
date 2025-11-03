from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, timedelta
# Create your views here.

class Task:
    def __init__(self, id, header, text, start_task, end_task):
        self.id = id
        self.header = header
        self.text = text
        self.start_task = start_task
        self.end_task = end_task
    
    def __str__(self):
        return f"""
            <h1>{self.header}</h1>
            <p>{self.text}</p>
            <p>{self.start_task}</p>
            <p>{self.end_task}</p>
        """

tasks = [
    Task(1, "Task1", "To Do", datetime.now(), datetime.now() + timedelta(days=10)),
    Task(2, "Task2", "To Do", datetime.now(), datetime.now() + timedelta(days=3)),
    Task(3, "Task3", "To Do", datetime.now(), datetime.now() + timedelta(days=6)),
    Task(4, "Task4", "To Do", datetime.now(), datetime.now() + timedelta(days=1)),
]

def index(request):
    return HttpResponse(tasks)