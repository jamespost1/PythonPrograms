# CSCI 220/620
# Summer 2022
# Assignment 2 - Functions, Sets, and Sums
# James Post


from itertools import product


def get_function_type(func, func_domain, func_co_domain):
    func_range = set()
    for element in func_domain:
        val = func(element)
        if val not in func_co_domain:
            return "Partial (and not total)"
        else:
            func_range.add(val)
    if len(func_domain) == len(func_range) and len(func_range) == len(func_co_domain):
        return "Bijective"
    elif func_range == func_co_domain:
        return "Surjective (and onto)"
    elif len(func_range) == len(func_domain):
        return "Injective (and one-to-one)"


def set_union(a, b):
    print("X U Y = ", a.union(b))


def set_intersection(a, b):
    print("X ∩ Y = ", a.intersection(b))


def set_difference(a, b):
    print("X - Y = ", a.difference(b))


def set_symmetric_difference(a, b):
    print("X ∆ Y = ", a.symmetric_difference(b))


def set_cartesian_product(a, b):
    cp = list(product(a, b))
    print("X  x  Y = ", str(cp))


def set_power_set(a):
    subsets = [[]]
    print("P(X) = ")
    for element in a:
        for idx in range(len(subsets)):
            subset = subsets[idx]
            subsets.append(subset + [element])
    return subsets


def flip_binary_digit(digit):
    return "1" if digit == "0" else "0"


def generate_binary_number(binary_numbers):
    max_size = max([len(number) - 2 for number in binary_numbers])
    new_number = "0."
    for index in range(len(binary_numbers)):
        if index >= max_size:
            new_number += "1"
        else:
            new_number += flip_binary_digit(binary_numbers[index][index + 2])
    return new_number


def sum_geometric_series(a, r, n):
    if r != 1:
        print("The sum of the geometric series is ", (((a*r)**(n+1)) - a)/(r-1))
    else:
        print("The sum of the geometric series is ", a*(n+1))


def sum_arithmetic_series(n, a, d):
    print("The sum of the arithmetic series is ", (n/2)*(2*a+(n-1)*d))


def sum_counting(n):
    print("The sum is: ", (n*(n+1))/2)


def sum_squares(n):
    print("The sum is: ", (n*(n+1)*(2*n+1))/6)


def sum_cubes(n):
    print("The sum is: ", (n**2*(n+1)**2)/4)


def main():
    x = {"a", "ab", "abc", "abcd"}
    y = {"a", "bb", "ccc", "dddd"}
    set_union(x, y)
    set_intersection(x, y)
    set_difference(x, y)
    set_symmetric_difference(x, y)
    set_cartesian_product(x, y)
    print(set_power_set(x))
    binary_numbers = ["0.010011", "0.101010", "0.111000", "0.000111", "0.111111", "0.111000"]
    print("New number is ", generate_binary_number(binary_numbers))
    sum_geometric_series(3, 1, 10)
    sum_arithmetic_series(10, 2, 2)
    sum_counting(100)
    sum_squares(10)
    sum_cubes(5)


if __name__ == "__main__":
    main()
