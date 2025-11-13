from django.shortcuts import render
from django.http import HttpRequest
from .forms import EventForm, ParticipantForm

def index(req):
    return render(req, "index.html", context={
        'event_form': EventForm() ,
        'participant_form': ParticipantForm()
    })

def post_event(req: HttpRequest):
    event_name = req.POST.get("name")
    event_date = req.POST.get("date")
    event_participants = req.POST.getlist("email")
    print(event_name, event_date, event_participants)
    return render(req, "event.html", context={
        "name": event_name,
        "date": event_date,
        "emails": event_participants
    });