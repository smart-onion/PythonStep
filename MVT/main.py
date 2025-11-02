from MVT.RecipeRepo import RecipeRepo
from MVT.RecipeTemplate import RecipeListTemplate, FullRecipeTemplate
from MVT.RecipeView import RecipeView
from Recipe import Recipe
repo = RecipeRepo()
app = RecipeView(repo)

def add_recipe() -> Recipe:
    return Recipe(input("Name: "), input("Description: "), input("Instruction: "))

while True:

    print("1 - Get List")
    print("2 - Get Detailed List")
    print("3 - Add ")
    print("4 - Remove")
    i = int(input("Select action: "))

    match i:
        case 1:
            app.render(RecipeListTemplate())
        case 2:
            app.render(FullRecipeTemplate())
        case 3:
            repo.add(add_recipe())
        case 4:
            repo.remove(input("Recipe Id: "))
        case _:
            break