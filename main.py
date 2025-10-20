import time


class Engine:
    def start_engine(self):
        print("Engine start")

    def stop_engine(self):
        print("Engine stop")


class Vehicle:
    def __init__(self, max_speed):
        self.max_speed = max_speed

    def drive(self):
        print(f"Driving with max speed {self.max_speed}")


class Car(Vehicle, Engine):
    def __init__(self, max_speed, model):
        Vehicle.__init__(self, max_speed)
        self.model = model

    def drive(self):
        print(f"Car {self.model} driving with max speed {self.max_speed}")


class Boat(Vehicle, Engine):
    def __init__(self, max_speed, boat_type):
        super().__init__(max_speed)
        self.type = boat_type

    def drive(self):
        print(f"Boat {self.type} driving with max speed {self.max_speed}")


class AmphibiousVehicle(Car, Boat):

    def __init__(self, max_speed, model, boat_type):
        Car.__init__(self, max_speed, model)
        Boat.__init__(self, max_speed, boat_type)
        self.is_on_land = True

    def drive(self):
        if self.is_on_land:
            Car.drive(self)
        else:
            Boat.drive(self)


am = AmphibiousVehicle(10, "asd", "asd")
am.is_on_land = True
am.drive()


class Book:
    def __init__(self, name: str, pages: int):
        self.name: str = name
        self.pages: int = pages

    def __ge__(self, other):
        return self.pages >= other.pages

    def __le__(self, other):
        return self.pages <= other.pages

    def __gt__(self, other):
        return self.pages > other.pages

    def __lt__(self, other):
        return self.pages < other.pages

    def __eq__(self, other):
        return self.pages == other.pages

    def __ne__(self, other):
        return self.pages != other.pages

    def __str__(self):
        return f"Name: {self.name} Pages: {self.pages}"


class Library:
    def __init__(self, books=None):
        self.books: [Book] = books if books is not None else []

    def __iadd__(self, other: Book):
        self.books.append(other)
        return self

    def __isub__(self, other: Book):
        self.books.remove(other)
        return self

    def __contains__(self, item: Book):
        return item in self.books

    def __len__(self):
        return len(self.books)

    def __str__(self):
        text = "Library:"
        for i in self.books:
            text += f"\n\t{i}"
        return text


lib = Library()

b1 = Book("MyFirst", 120)
b2 = Book("Second", 130)

lib += b1
lib += b2

lib -= b1


def cache_decorator(func):
    storage = {}

    def wrapper(*args, **kwargs):
        args_hash = hash(args) + hash(tuple(kwargs))
        if args_hash in storage:
            return storage[args_hash]
        result = func(*args, **kwargs)
        storage[args_hash] = result
        return result

    return wrapper


def cache_class_methods(cls):
    for f, method in cls.__dict__.items():
        if callable(method):
            try:
                setattr(cls, f"{f}", cache_decorator(method))
            except TypeError:
                pass
    return cls


@cache_class_methods
class Test:
    def __init__(self):
        pass

    def foo(self, x, y):
        return x + y


a = Test()
print(a.foo(1, 1))
print(a.foo(1, 1))
print(a.foo(1, 2))
