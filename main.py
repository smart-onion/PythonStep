from typing import get_type_hints
import time


def type_validator(func):
    def wrapper(*args):
        annotation: dict[str, type] = get_type_hints(func)
        for t, i in zip(annotation.values(), args):
            if t != type(i):
                raise TypeError(f"{i} not type of {t}")
        return func(*args)

    return wrapper


def cache(func):
    storage = {}

    def wrapper(*args, **kwargs):
        args_hash = hash(args) + hash(tuple(kwargs))

        if args_hash in storage:
            return storage[args_hash]

        result = func(*args, **kwargs)
        storage[args_hash] = result
        return result

    return wrapper


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


def authorize(func):
    user_db: [User] = [User("alex", "123456"), User("bob", "1234")]

    def wrapper(user: User, *args, **kwargs):
        for credentials in user_db:
            if credentials.username == user.username and credentials.password == user.password:
                return func(user, *args, **kwargs)
        raise Exception("Not authorized")

    return wrapper


def try_again(count: int):
    def inner(func):
        def wrapper(*args, **kwargs):
            attempts_left = count
            while attempts_left != 0:
                try:
                    return func(*args, **kwargs)
                except Exception as ex:
                    print(ex)
                    attempts_left -= 1
            return Exception

        return wrapper

    return inner


@try_again(4)
def add(user: User, x, y):
    return x + y


def fibonachi():
    last = 1
    prev = 0
    while True:
        number = last + prev
        prev = last
        last = number
        yield number


a = fibonachi()
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print("\n\n\n/////////////////////////////////////////////////")


def multiple_to_3_and_5(limit: int = 1000):
    for i in range(1, limit):
        if i % 3 == 0 and i % 5 == 0:
            yield i


b = multiple_to_3_and_5()
print(next(b))


def infinite_factorial():
    number = 1
    result = 1
    while True:
        result = number * result
        number += 1
        yield result


c = infinite_factorial()
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))


def only_element(index: int, elems: list):
    current = 0
    for i in elems:
        if current != 0 and current % index == 0:
            yield i
        current += 1


d = only_element(3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(next(d))
print(next(d))
print(next(d))


def closing_limit():
    limit = 3

    def inner():
        nonlocal limit
        if limit == 0:
            print("Limit of function call exceeded")
            return

        print(f"Doing some job {limit}")
        limit -= 1
        return

    return inner


closing = closing_limit()
closing()
closing()
closing()
closing()
closing()


def is_number_in_numbers(numbers: [int]):
    def inner(number: int):
        return number in numbers

    return inner


numbers = is_number_in_numbers([12, 3, 4, 45, 65])

print(numbers(12))
print(numbers(1234))


def string_formatter(template: str):
    def inner(**kwargs):
        return template.format(**kwargs)

    return inner


frm = string_formatter("Hi {name}!")

print(frm(name="Alex"))


def difference():
    prev = 0

    def inner(number: int):
        nonlocal prev
        prev = number - prev
        return prev

    return inner


deff = difference()

print(deff(1))
print(deff(2))
print(deff(24))
print(deff(23))

print("\n///////////////////////////////////////////////////////////////////\n\n")


def unique_call():
    called_storage = []

    def inner(*args, **kwargs):
        nonlocal called_storage
        args_hash = hash(args) + hash(tuple(kwargs))
        if args_hash not in called_storage:
            called_storage.append(args_hash)
        return len(called_storage)

    return inner


unique = unique_call()

print(unique(1))
print(unique(2))
print(unique(3))
print(unique(3))
print(unique(3, 2))
print(unique(3))
