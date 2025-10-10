class Book:
    __slots__ = ("__name", "__author", "__total_pages")

    def __init__(self, name: str, author: str, total_pages: int):
        self.__name: str = name
        self.__author = author
        self.__total_pages = total_pages

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def author(self): return self.__author

    @author.setter
    def author(self, author: str):
        self.__author = author

    @property
    def total_pages(self): return self.__name

    @total_pages.setter
    def total_pages(self, name: str):
        self.__name = name

    def get_info(self):
        print(f"Name: {self.__name}\nAuthor: {self.__author}\nTotal Pages: {self.total_pages}")

    def is_more_then_300(self) -> bool:
        return self.__total_pages > 300


book = Book("Name", "Author", 301)
book.get_info()


class Counter:
    def __init__(self):
        self.__count = 0

    def increment(self):
        self.__count += 1

    def decrement(self):
        self.__count -= 1

    def reset(self):
        self.__count = 0

    def get_value(self):
        return self.__count


class Calculator:
    @staticmethod
    def add(a: int, b: int) -> int:
        return a + b

    @staticmethod
    def subtract(a: int, b: int) -> int:
        return a - b

    @staticmethod
    def multiply(a: int, b: int) -> int:
        return a * b

    @staticmethod
    def divide(a: int, b: int) -> float:
        if b == 0:
            print("ZeroDivisionError")
        return a / b


class Rectangle:
    def __init__(self, width: float, height: float):
        self.__width = width
        self.__height = height

    def area(self): return self.__width * self.__height

    def perimeter(self): return (self.__width * 2) + (self.__height * 2)

    def is_square(self): return self.__width == self.__height


class BankAccount:
    def __init__(self, name: str, balance: float):
        self.__name = name
        self.__balance = balance

    def deposit(self, amount: float):
        self.__balance += amount

    def withdraw(self, amount: float):
        self.__balance = self.__balance - amount if self.__balance >= amount else self.__balance

    def display_balance(self):
        print(f"Current balance: {self.__balance}")