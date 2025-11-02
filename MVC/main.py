from unittest import case

from MVC.CostController import CostController
from MVC.CostRepo import CostRepo
from MVC.CostView import CostView

repo = CostRepo()
view = CostView()
app = CostController(repo, view)

while True:

    print("1 - Get All Costs")
    print("2 - Get Total Costs")
    print("3 - Add Cost")
    print("4 - Remove Cost")
    i = int(input("Select action: "))

    match i:
        case 1:
            app.get_costs()
        case 2:
            app.get_total_cost()
        case 3:
            app.add_cost()
        case 4:
            app.remove_cost()
        case _:
            break