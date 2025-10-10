import json

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


# book = Book("Name", "Author", 301)
# book.get_info()


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


# /////////////////////////////////////////////////////////////////

class Library:
    def __init__(self):
        self.__library: [Book] = []

    def add_book(self, book: Book):
        self.__library.append(book)

    def remove_book_by_name(self, name: str):
        self.__library = filter(lambda b: b.name != name, self.__library)

    def get_book_by_name(self, name: str) -> Book:
        for book in self.__library:
            if book.name == name:
                return book


class Dish:
    def __init__(self, name: str, price: float, category: str):
        self.__name = name
        self.__price = price
        self.__category = category

    def info(self):
        print(f"Name: {self.__name}\nprice: {self.__price}\ncategory: {self.__category}")

    @property
    def name(self): return self.__name
    @property
    def price(self): return self.__price
    @property
    def category(self): return self.__category


class Order:
    def __init__(self):
        self.__orders: [Dish] = []

    def add_dish(self, dish: Dish):
        self.__orders.append(dish)

    def remove_dish_by_name(self, name: str):
        self.__orders = filter(lambda b: b.name != name, self.__orders)

    def total_bill(self):
        total = 0
        for i in self.__orders:
            total += i.price
        return total

class Restorant:
    def __init__(self):
        self.__menu: [Dish] = []

    def add_dish_to_menu(self, dish: Dish):
        self.__menu.append(dish)

    def show_menu(self):
        for dish in self.__menu:
            print(f"Name: {dish.name}\n\tPrice: {dish.price}\n\tCategory: {dish.category}")


class Student:
    def __init__(self, name, age):
        self.name: str = name
        self.age: int = age
        self.scores: [int] = []

    def average_score(self) -> float:
        return sum(self.scores) / self.scores.count()

class StudentDatabase:
    def __init__(self):
        self.__students: [Student] = []

    def add_student(self, student: Student):
        self.__students.append(student)

    def get_students(self, student_name: str):
        return self.__students

    def find_student_by_name(self, name:srt):
        for student in self.__students:
            if student.name == name:
                return student
