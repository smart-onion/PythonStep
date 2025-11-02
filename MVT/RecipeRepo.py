import functools
import json
import os
from functools import wraps
from typing import List

from Recipe import Recipe, RecipeEncoder


def load(path) -> List[Recipe]:
    try:
        with open(path, "r") as f:
            json_load: List[Recipe] = json.load(f)
        l = []
        for r in json_load:
            l.append(Recipe(r["name"], r["description"],r["instruction"], r["ingredients"],r["id"] ))
        return l
    except:
        return []


class RecipeRepo:
    path = "RecipeRepo.json"
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls, *args, **kwargs)
        return cls.__instance

    def __init__(self):
        if not hasattr(self, "exist"):
            self.exist = True
            self.recipies: List[Recipe] = load(RecipeRepo.path)
            pass

    def save(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            result = func(self, *args, **kwargs)
            with open(RecipeRepo.path, "w") as f:
                j = json.dumps(self.recipies, indent=4, cls=RecipeEncoder)
                f.write(j)
            return result
        return wrapper


    @save
    def add(self, e: Recipe):
        self.recipies.append(e)


    @save
    def remove(self, id: str):
        r = [i for i in self.recipies if i.id == id][0]
        if r is None:
            return False
        self.recipies.remove(r)
        return True

    def get_all(self):
        return self.recipies