from uuid import uuid4

class Cost:
    def __init__(self, amount: int, description: str):
        self.id: str = str(uuid4())[:5]
        self.amount: int = amount
        self.description = description

    def __str__(self):
        return f"Id: {self.id}\n{self.amount} - {self.description}"