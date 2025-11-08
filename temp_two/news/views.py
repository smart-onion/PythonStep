from django.shortcuts import render
from django.http import HttpResponseNotFound
from uuid import uuid4

class News:
    def __init__(self, title, text, category, image):
        self.id = str(uuid4())
        self.title = title
        self.text = text
        self.category = category
        self.image = image

categories=[
    "Sport",
    "World",
    "Nature",
    "Space"
]

news = [
    News("Sport One", "Some text about sport one", "Sport", "sport.jpg"),
    News("Sport Two", "Some text about sport Two", "Sport", "sport.jpg"),
    News("Sport Tree", "Some text about sport Tree", "Sport", "sport.jpg"),
    News("Sport Four", "Some text about sport Four", "Sport", "sport.jpg"),
    News("World One", "Some world one news", "World", "world.jpg"),
    News("World One", "Some world one news", "World", "world.jpg"),
    News("World One", "Some world one news", "World", "world.jpg"),
    News("World One", "Some world one news", "World", "world.jpg"),
    News("Nature One", "Some Nature one news", "Nature", "nature.jpg"),
    News("Nature One", "Some Nature one news", "Nature", "nature.jpg"),
    News("Nature One", "Some Nature one news", "Nature", "nature.jpg"),
    News("Nature One", "Some Nature one news", "Nature", "nature.jpg"),
    News("Nature One", "Some Nature one news", "Nature", "nature.jpg"),
    News("Nature One", "Some Nature one news", "Nature", "nature.jpg"),
]

def index(req):
    return render(req, 'index.html', context={"categories": categories})

def category_page(req, category):
    n = list(filter(lambda x : x.category == category, news))
    return render(req, "category.html", context={"news": n})

def curr_news(req,category, id):
    for i in news:
        if i.id == id:
            return render(req, "current_news.html", context={"news": i})
    return HttpResponseNotFound()
    