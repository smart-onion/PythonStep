from typing import List

from Cost import Cost
from CostRepo import CostRepo
from CostView import CostView

class CostController:
    def __init__(self, repo: CostRepo, view: CostView) -> None:
        self.repo: CostRepo = repo
        self.view: CostView = view

    def get_costs(self) -> None:
        costs = self.repo.get_costs()
        return self.view.get_costs(costs)

    def add_cost(self) -> None:
        cost = self.view.add_cost()
        self.repo.add_cost(cost)
        return self.view.get_costs(self.repo.get_costs())

    def remove_cost(self) -> None:
        id = self.view.delete_cost()
        self.repo.delete_cost(id)
        return self.view.get_costs(self.repo.get_costs())

    def get_total_cost(self):
        return self.view.get_total_cost(self.repo.get_total_cost())