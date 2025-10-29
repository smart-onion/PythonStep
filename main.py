class PositiveValue:
    def __get__(self, instance, instance_type):
        print("sd")
        return instance.value

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError("Value can't be less then 0")
        instance.value = value


class Name:
    def __get__(self, instance, owner):
        return instance.value

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("Name mast be a string")

        if value.isalpha() and value[0].isupper():
            instance.value = value
            return
        raise ValueError("Name mast start from upper letter and letters only")


class BankAccount:
    __balance = PositiveValue()
    name = Name()

    def __init__(self, name: str, amount: int):
        self.name = name
        self.__balance = amount

    def check_balance(self):
        return self.__balance


b = BankAccount("Asd", 10)


class LogDescriptor:
    def __get__(self, instance, owner):
        print(f"Reading from {instance}")
        return instance.value

    def __set__(self, instance, value):
        print(f"Writing to {instance}")
        instance.value = value


class LogTester:
    log = LogDescriptor()

    def __init__(self):
        self.log = 1


class WithoutUnderscore(type):
    def __new__(cls, name, bases, attrs: dict):
        print(attrs)
        for attr in attrs.keys():
            if attr.startswith("_") and not attr.startswith("__") and not attr.endswith("__"):
                raise ValueError("Attribute can't start with '_'")

        return super().__new__(cls, name, bases, attrs)


class TestAttributes(metaclass=WithoutUnderscore):
    a = 1


class HelloMetaClass(type):
    def __new__(cls, name, bases, attrs: dict):
        attrs["hello"] = lambda x: print("Hello")
        return super().__new__(cls, name, bases, attrs)


class TestHello(metaclass=HelloMetaClass):
    pass


TestHello().hello()


class NoForbiddenInherit(type):
    def __new__(cls, name, bases, attrs: dict):
        for base in bases:
            if "Forbidden" in base.__name__:
                raise TypeError("Can't inherit from class with 'Forbidden' in name")


class ForbiddenClass:
    pass


# class TestNoForbiddenInherit(ForbiddenClass, metaclass=NoForbiddenInherit):
#     pass


class StringAttributesOnly(type):
    def __new__(cls, name, bases, attrs: dict):
        for v in attrs.values():
            if not isinstance(v, str):
                raise ValueError("String allowed only")


class TestStringOnly(metaclass=StringAttributesOnly):
    a = "test"
    # b = 12


from typing import Protocol, runtime_checkable
from abc import ABC, abstractmethod


@runtime_checkable
class Shape(Protocol):
    @abstractmethod
    def area(self) -> int: raise NotImplemented


class Rectangle(Shape):
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    def area(self) -> int:
        return self.a * self.b


a = Rectangle(1, 2)


def test_protocol(shape: Shape) -> None:
    print(shape.area() * 2)


test_protocol(a)


class Circle(Shape):
    __PI = 3.14

    def __init__(self, r):
        self.r = r

    def area(self) -> int:
        return (2 * self.__PI * (self.r ** 2)) / 2

    @property
    def pi(self): return self.__PI


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self) -> int:
        return 0.5 * self.base * self.height


def print_area(shape: Shape) -> None:
    print(shape.area())


class Serializable(Protocol):
    def serialize(self) -> str: pass


import json


class Book(Serializable):
    def __init__(self, name):
        self.name = name
        self.tt = 123

    def serialize(self):
        return json.dumps(self.__dict__)


class Person(Serializable):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def serialize(self) -> str:
        return json.dumps(self.__dict__)


def serialize_object(obj: Serializable):
    print(obj.serialize())


serialize_object(Book("ased"))
