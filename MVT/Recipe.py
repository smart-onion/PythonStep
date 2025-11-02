import json
from typing import List
from uuid import uuid4

class Recipe:
    def __init__(self, name:str, description:str, instruction: str, ingredients=None, id=None):
        if ingredients is None:
            ingredients = []
        self.id: str = str(uuid4()) if id is None else id
        self.name: str = name
        self.description: str = description
        self.ingredients: List[str] = ingredients
        self.instruction: str = instruction

    def __str__(self) -> str:
        return f"id: {self.id}\nname: {self.name}\ndescription: {self.description}\ningredients: {self.ingredients}\ninstruction: {self.instruction}"


class RecipeEncoder(json.JSONEncoder):
    def default(self, obj: Recipe):
        return obj.__dict__