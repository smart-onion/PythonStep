from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta
import random
# Create your views here.

class Task:
    def __init__(self, header, text, start_task, end_task, id=None):
        self.id = id if id is not None else random.randint(10, 100000)
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
            <a href="remove/{self.id}">remove</a>
        """

tasks = [
    Task("Task1", "To Do", datetime.now(), datetime.now() + timedelta(days=10)),
    Task("Task2", "To Do", datetime.now(), datetime.now() + timedelta(days=3)),
    Task("Task3", "To Do", datetime.now(), datetime.now() + timedelta(days=6)),
    Task("Task4", "To Do", datetime.now(), datetime.now() + timedelta(days=1)),
]

def index(request):
    
    return HttpResponse(tasks)


@csrf_exempt
def add_task(request: HttpRequest):
    if request.method == "POST":
        header = request.POST.get("header")
        text = request.POST.get("text")
        start_task = request.POST.get("start_task")
        end_task = request.POST.get("end_task")
        tasks.append(Task(header, text, start_task, end_task))

    html = f"""
        <form method="post">
        <input type="text" name="header" />
        <input type="text" name="text" />
        <input type="date" name="start_task" />
        <input type="date" name="end_task" />
        <input type="submit" value="Add" />
    </form>
    {''.join([f"<p>{x}</p>" for x in tasks])}
    """
    
    return HttpResponse(html)

@csrf_exempt
def remove_task(request: HttpRequest, id: int):
    global tasks
    tasks = list(filter(lambda x: x.id != id, tasks))

    return redirect("index")