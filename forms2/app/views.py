from django.shortcuts import render, redirect
from .forms import FilmForm
from django.http import HttpRequest, HttpResponseBadRequest
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
from datetime import datetime
from uuid import uuid4
class Film:
    id: str
    name: str
    description: str
    issued: datetime
    country: str
    image: str

    def __init__(self, name, description, issued, country, image):
        self.id = str(uuid4())
        self.name = name
        self.description = description
        self.issued = issued
        self.country = country
        self.image = image

films = [

]

def get_current_timestamp():
    return str(int(datetime.timestamp(datetime.now())))

def get_add_film(req):
    return render(req, "add_film.html", context={'form': FilmForm()})


def post_add_film(req: HttpRequest):
    if req.method == "POST":
        filmForm = FilmForm(req.POST, req.FILES)
        if filmForm.is_valid():
            name = filmForm.cleaned_data["name"]
            description = filmForm.cleaned_data["description"]
            issued = filmForm.cleaned_data["issued"]
            country = filmForm.cleaned_data["country"]
            image = filmForm.cleaned_data["image"]
            fs = FileSystemStorage(location=settings.MEDIA_ROOT)
            file_name = fs.save(get_current_timestamp() + '__' + image.name, image)
            film = Film(name, description, issued, country, fs.url(file_name))
            films.append(film)
            return redirect(f'film/{film.id}')
        return HttpResponseBadRequest()

def show_film(req, id):
    f = list(filter(lambda x : x.id == id, films))[0]
    return render(req, "film.html", context={'film': f})

def index(req: HttpRequest):
    return render(req, "index.html", context={'films':films })