# Task 1
def number_count(number: int) -> int:
    result = 0

    def inner(current_number: int, current_result: int) -> int:
        if current_number < 1:
            return current_result
        return inner(current_number / 10, current_result + 1)

    return inner(number, result)


print(number_count(1234))


# Task 2
def substring_count(string: str) -> dict[str, int]:
    exceptions = list(".,?!")

    string_arr = string.split()

    result: dict[str, int] = {}
    for i in string_arr:
        i = i[:-1] if i[-1] in exceptions else i

        result[i] = result[i] + 1 if i in result else 1

    return result


print(substring_count("Hi tom, my name is tom! One one one one"))

# Task 3
numbers: list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_number = list(filter(lambda x: x % 2 == 0, numbers))
squares = list(map(lambda x: x ** 2, even_number))
print(squares)

# Task 4
students: dict[str, list[int]] = {
    "Alex": [6, 5, 34, 76, 78, 4, 2, ],
    "Bob": [34, 1234, 67, 23, 234],
    "Tom": [6, 5, 34, 6, 8, 4, 3, 5, 6, 78, 4, 2, ]
}

for k, v in students.items():
    average = round(sum(v) / len(v), 2)
    print(f"Average of {k} = {average}")


# Task 5
def count_of_symbols(string: str) -> dict[str, int]:
    arr = list(string)
    result: dict[str, int] = {}
    for i in arr:
        result[i] = result[i] + 1 if i in result else 1
    return result


print(count_of_symbols("Heeeee waa"))

# Task 6
my_tuple = ("str", 1, 2, "asd", 1)


def new_tuple(t: tuple) -> tuple:
    return tuple(filter(lambda x: type(x) is int, t))


print(new_tuple(my_tuple))

# Task 7

unsorted_list = ["as", "a", "asd asd", "asdq"]


def sorted_string_by_len(strings: [str]) -> [str]:
    return sorted(strings, key=len)


print(sorted_string_by_len(unsorted_list))

# Task 8
employees: dict[str, (str, float)] = {
    "Alex": ("one", 1000),
    "Bob": ("tree", 3000),
    "Tom": ("two", 2000),
}


def sorted_by_salary(emp: dict[str, (str, float)]) -> dict[str, (str, float)]:
    return dict(sorted(emp.items(), key=lambda i: i[1][1]))


print(sorted_by_salary(employees))

# Task 9

bigger = lambda x, y: x if x > y else y

print(bigger(6, 2))

l = [1, 1, 1, 1, 2, 2, 3]


# Task 10
def unique(l: list) -> set:
    return set(l)


print(unique(l))


# Task 11

def create_dict_of_squares(max=10) -> dict[int, int]:
    result: dict[int, int] = {}
    for i in range(max):
        result[i] = i ** 2

    return result


print(create_dict_of_squares())


def sum_of_squares_dict(d: dict[int, int]) -> tuple[int, int]:
    sum_k = 0
    sum_v = 0
    for k, v in d.items():
        sum_k += k
        sum_v += v
    return (sum_k, sum_v)


print(sum_of_squares_dict(create_dict_of_squares()))

# Task 12

list_12 = [1, 2, 3, 4, 12, 23, 2123, 123, 1, 20, 16]


def more_then_ten_and_even(l: list) -> list:
    return [i for i in l if i > 10 and i % 2 == 0]


print(more_then_ten_and_even(list_12))

# Task 13

tuple_13 = (10, 20, 30)


def sum_of_tuple(t: tuple) -> int:
    return sum(t)


print(sum_of_tuple(tuple_13))

# Task 14

is_positive = lambda x: True if x > 0 else False

print(is_positive(1))

# Task 15

dict_15 = {
    "Tom": 12,
    "Alex": 13,
    "Bob": 14,
    "Red": 15,
}


def more_then_age(age: int, collection: dict[str, int]) -> list[str]:
    return [k for k, v in collection.items() if v > age]


print(more_then_age(13, dict_15))

# Task 16

tuple_16 = (1, 23, 4, 5, 4, 35, 123, 12, 5, 1, 4)


def max_and_min_of_tuple(t: tuple) -> tuple:
    return (min(t), max(t))


print(max_and_min_of_tuple(tuple_16))

# Task 17
list_17 = [12, 123, 9, 4534, 5, 123, 23]

result_17 = list(filter(lambda x: x % 3 == 0, list_17))
print(result_17)


# Task 18
def list_of_tuple(string: str) -> list[tuple]:
    return [(value, i) for i, value in enumerate(string, start=0)]


print(list_of_tuple("Hello world!"))
