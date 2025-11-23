from django.shortcuts import render, redirect
from .forms import FilmForm
from django.http import HttpRequest, HttpResponseBadRequest, HttpResponseNotFound
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
from datetime import datetime
from uuid import uuid4
from .models import Film



# Film.objects.create(
#     name="count", 
#     description = "earth seeing growth steep that doll subject pretty poem burn wing compare pure bring sent diagram nearly term tight cell seen hospital behind time",
#     country="St. Martin",
#     rating=2,
#     issued=datetime.now()
#     )



def get_current_timestamp():
    return str(int(datetime.timestamp(datetime.now())))

def get_add_film(req):
    return render(req, "add_film.html", context={'form': FilmForm()})


def post_add_film(req: HttpRequest):
    if req.method == "POST":
        filmForm = FilmForm(req.POST, req.FILES)
        print(filmForm)
        if filmForm.is_valid():
            name = filmForm.cleaned_data["name"]
            description = filmForm.cleaned_data["description"]
            issued = filmForm.cleaned_data["issued"]
            country = filmForm.cleaned_data["country"]
            image = filmForm.cleaned_data["image"]
            rating = filmForm.cleaned_data["rating"]
            fs = FileSystemStorage(location=settings.MEDIA_ROOT)
            file_name = fs.save(get_current_timestamp() + '__' + image.name, image)
            # film = Film(name, description, issued, country, fs.url(file_name), rating)
            film = Film.objects.create(
                name=name, 
                description = description,
                country=country,
                rating=rating,
                issued=issued,
                image=fs.url(file_name)
                )
            film.save()
            return redirect(f'film/{film.id}')
        return HttpResponseBadRequest()

# def update_film(req: HttpRequest):
#     print("ASDASDASDASD")
#     form = req.GET.get("update_id")
#     try:
#         print("ID: " + form )
#         film = Film.objects.get(id=form)
        
#         return render(req, "add_film.html", context={'form': FilmForm(instance=film)})
#     except Film.DoesNotExist:
#         return HttpResponseNotFound("film not exist update")


def delete_film(req: HttpRequest):
    form = req.GET.get("delete_id")
    try:
        film = Film.objects.get(id=form)
        film.delete()
        return redirect("index")
    except Film.DoesNotExist:
        return HttpResponseNotFound("film not exist")
        

def show_film(req: HttpRequest, id):
    films = Film.objects.all()
    f = list(filter(lambda x : str(x.id) == id, films))[0]
    return render(req, "film.html", context={'film': f})


def index(req: HttpRequest):
    sort = req.GET.get("sort")
    films = Film.objects.all()
    if sort == "rating":
        films = films.order_by("-rating")
    elif sort == "issued":
        films = films.order_by("-issued")
    return render(req, "index.html", context={'films':films })