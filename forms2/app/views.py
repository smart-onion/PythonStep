from django.shortcuts import render, redirect
from .forms import FilmForm, GanreForm, CommentForm
from django.http import HttpRequest, HttpResponseBadRequest, HttpResponseNotFound, HttpResponseNotAllowed, HttpResponse, HttpResponseForbidden
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os
from datetime import datetime
from uuid import uuid4
from .models import Film, Ganre, Comment


def post_only(f):
    def wrapper(req: HttpRequest, *args, **kwargs):
        if req.method != "POST":
            return HttpResponseNotAllowed("POST only")
        return f(req, *args, **kwargs);
    return wrapper

def with_permition(permition: str):
    def inner(func):
        def wrapper(req: HttpRequest, *args, **kwargs):
            if req.user.has_perm(permition):
                return func(req, *args, **kwargs)
            return HttpResponseForbidden()
        return wrapper
    return inner

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
            ganre = filmForm.cleaned_data["ganre"]
            fs = FileSystemStorage(location=settings.MEDIA_ROOT)
            file_name = fs.save(get_current_timestamp() + '__' + image.name, image)
            # film = Film(name, description, issued, country, fs.url(file_name), rating)
            film = Film.objects.create(
                name=name, 
                description = description,
                country=country,
                rating=rating,
                issued=issued,
                image=fs.url(file_name),
                ganre=ganre
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
    comments = Comment.objects.filter(film_id=id)
    return render(req, "film.html", context={'film': f, "comment_form": CommentForm(initial={"film": f.id}), "comments": comments})


def index(req: HttpRequest):
    sort = req.GET.get("sort")
    films = Film.objects.all()
    if sort == "rating":
        films = films.order_by("-rating")
    elif sort == "issued":
        films = films.order_by("-issued")
    return render(req, "index.html", context={'films':films })


@post_only
def post_create_ganre(req: HttpRequest):
    g_name = req.POST.get("name")
    Ganre.objects.create(name=g_name)
    return redirect("all_ganres")

def get_create_ganre(req: HttpRequest):
    return render(req, "create_ganre.html", context={"form": GanreForm()})

def get_all_ganres(req):
    ganres = Ganre.objects.all()
    return render(req, "all_ganres.html", context={"ganres": ganres})   

@post_only
def post_create_comment(req: HttpRequest):
    form = CommentForm(req.POST)
    if form.is_valid():
        film_id = form.cleaned_data["film"]
        user_name=form.cleaned_data["user_name"]
        text=form.cleaned_data["text"]
        film = Film.objects.get(id=film_id)

        c = Comment.objects.filter(user_name__startswith=user_name).count()

        Comment.objects.create(film=film, user_name=f"{user_name}_{c}", text=text).save()
        return redirect(f"film/{film_id}")
    return HttpResponseBadRequest()

@with_permition("app.can_moderate_comments")
def delete_comment(req: HttpRequest, comment_id):
    try:
        comment = Comment.objects.get(id=comment_id)
        comment.delete()
        return redirect("index")
    except Comment.DoesNotExist:
        return HttpResponseNotFound()
    
