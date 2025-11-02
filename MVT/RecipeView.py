from MVT.RecipeRepo import RecipeRepo
from MVT.RecipeTemplate import RecipeTemplate


class RecipeView:
    def __init__(self,repo: RecipeRepo):
        self.repo: RecipeRepo = repo

    def render(self, template: RecipeTemplate):
        return template.render(self.repo.get_all())

