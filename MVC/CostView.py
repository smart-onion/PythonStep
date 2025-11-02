from Cost import Cost
from typing import List

class CostView:
    def add_cost(self) -> Cost:
        price: int = int(input("Enter price: "))
        description: str = input("Enter description: ")
        return Cost(price, description)

    def delete_cost(self) -> str:
        return input("Enter cost id: ")

    def get_costs(self, costs: List[Cost]) -> None:
        if len(costs) < 1:
            print("No costs")
            return
        for cost in costs:
            print("-"*25)
            print(cost)
            print("-"*25)

    def get_total_cost(self, amount: int) -> int:
        print("-"*25)
        print(f"Total cost: {amount}")
        print("-"*25)

