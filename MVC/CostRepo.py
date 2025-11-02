import Cost
from typing import List


class CostRepo:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'instantiated'):
            self.instantiated = True
            self.costs: List[Cost] = []

    def add_cost(self, cost: Cost.Cost):
        self.costs.append(cost)

    def delete_cost(self, id: str):
        cost = [x for x in self.costs if x.id == id]
        if cost[0] is None:
            return False
        self.costs.remove(cost[0])
        return True

    def get_costs(self) -> List[Cost.Cost]: return self.costs

    def get_total_cost(self) -> int: return sum(map(lambda c: c.amount, self.costs))


