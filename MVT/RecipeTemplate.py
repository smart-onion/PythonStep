from typing import Protocol, List
from Recipe import Recipe

class RecipeTemplate(Protocol):
    def render(self, obj): pass

class RecipeListTemplate(RecipeTemplate):
    def render(self, obj: List[Recipe]):
        for recipe in obj:
            print("-" * 25)
            print(recipe.name)
            print("-" * 25)

class FullRecipeTemplate(RecipeTemplate):
    def render(self, obj: List[Recipe]):
        for recipe in obj:
            print("-" * 25)
            print(recipe)
            print("-" * 25)