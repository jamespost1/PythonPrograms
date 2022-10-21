# CSCI 220/620
# Summer 2022
# Assignment 7 - Recurrence Relations
# James Post
import math


dict_funcs = {}


def eval_func(func, n):
    func_name = func.__name__
    if func_name not in dict_funcs:
        dict_funcs[func_name] = {}
    dict_func = dict_funcs[func_name]
    if n not in dict_func:
        dict_func[n] = func(func, n)
    return dict_func[n]


def f1_merge_sort(func, n):
    if n == 1:
        return 0
    else:
        return 2 * eval_func(func, int(n/2)) + n


def f2_binary_search(func, n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return eval_func(func, int(n/2)) + 2


def f3_fibonacci(func, n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return eval_func(func, n-1) + eval_func(func, n-2)


def f4_bit_strings(func, n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        return eval_func(func, n-1) + eval_func(func, n-2)


def f5_midterm_summer_2021(func, n):
    if n == 1:
        return 2
    else:
        return 4 * eval_func(func, int(n / 3)) + n


def f6_midterm_winter_2022(func, n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return 125 * eval_func(func, int(n/5)) + 5*n


def f7_hanoi(func, n):
    if n == 1:
        return 1
    else:
        return 2 * eval_func(func, n-1) + 1


def f8_catalan(func, n):
    if n == 0 or n == 1:
        return 1
    else:
        s = 0
        for k in range(0, n):
            s += eval_func(func, k) * eval_func(func, n-k-1)
        return s


def f9_slide_22(func, n):
    if n == 0:
        return 2
    elif n == 1:
        return 7
    else:
        return eval_func(func, n-1) + 2*eval_func(func, n-2)


def f10_bubble_sort(func, n):
    if n == 1:
        return 0
    else:
        return eval_func(func, n-1) + (n - 1)


def f11_sum_squares(func, n):
    if n == 1:
        return 1
    else:
        return eval_func(func, n-1) + n**2


def f12_sum_cubes(func, n):
    if n == 1:
        return 1
    else:
        return eval_func(func, n-1) + n**3


def f13_exam1_fall_2008(func, n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return 8*eval_func(func, int(n/4)) + n


def f14_parallel_merge_sort(func, n):
    if n == 0 or n == 1:
        return 0
    else:
        return eval_func(func, int(3*n / 4)) + int(math.log2(n))


def f15_final_2008(func, n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return 9 * eval_func(func, int(n/3)) + n


def f16_exam1_2008(func, n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return 9 * eval_func(func, int(n/4)) + n


def f17_final_2008(func, n):
    if n == 0:
        return 1
    else:
        s = 1
        for k in range(0, n):
            s += 3+eval_func(func, k)
        for k in range(1, n+1):
            s += 1 + 3*eval_func(func, k-1)
        return s


def f18_exam1_2016(func, n):
    if n == 0 or n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return 2 * eval_func(func, n-1) + 3 * eval_func(func, n-2)


def call_and_print(func, n, desc):
    print(func.__name__, desc, "for n =", n, "is", eval_func(func, n))


def print_dict(dic):
    for key in dic:
        print(key, dic[key])


def traditional_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return traditional_fibonacci(n-1) + traditional_fibonacci(n-2)


def main():
    call_and_print(f1_merge_sort, 256, "f(1) = 0, f(n) = 2*f(n/2) + n")
    call_and_print(f2_binary_search, 256, "f(1) = 1, f(n) = f(n/2) + 2")
    call_and_print(f3_fibonacci, 256, "f(0) = 0, f(1) = 1, f(n) = f(n-1) + f(n-2)")
    call_and_print(f4_bit_strings, 256, "f(0) = 1, f(1) = 2, f(n) = f(n-1) + f(n-2)")
    call_and_print(f5_midterm_summer_2021, 256, "f(1) = 2, f(n) = 4f(n/3) + n")
    call_and_print(f6_midterm_winter_2022, 256, "f(1) = 1, f(n) = 125f(n/5) + 5n")
    call_and_print(f7_hanoi, 256, "f(1) = 1, f(n) = 2f(n-1) + 1")
    call_and_print(f8_catalan, 256, "f(0) = 1, f(1) = 1, f(n) = sum[f(k)*f(n-k-1)]")
    call_and_print(f9_slide_22, 256, "f(0) = 2, f(1) = 7, f(n) = f(n-1) + 2*f(n-2)")
    call_and_print(f10_bubble_sort, 256, "f(1) = 0, f(n) = f(n-1) + (n-1)")
    call_and_print(f11_sum_squares, 256, "f(1) = 1, f(n) = f(n-1) + n^2")
    call_and_print(f12_sum_cubes, 256, "f(1) = 1, f(n) = f(n-1) + n^3")
    call_and_print(f13_exam1_fall_2008, 256, "f(1) = 1, f(n) = 8*f(n/4) + n")
    call_and_print(f14_parallel_merge_sort, 256, "f(0) = 0, f(1) = 0, f(n) = f(3n/4) + log(n)")
    call_and_print(f15_final_2008, 256, "f(1) = 1, f(n) = 9*f(n/3) + n")
    call_and_print(f16_exam1_2008, 256, "f(1) = 1, f(n) = 9*f(n/4) + n")
    call_and_print(f17_final_2008, 256, "f(0) = 1, f(n) = sum[3 + f(k)]etc")
    call_and_print(f18_exam1_2016, 256, "f(0) = 1, f(2) = 2, f(n) = 2f(n-1) + 3f(n-2)")
    print_dict(dict_funcs)
    print(traditional_fibonacci(10))


if __name__ == "__main__":
    main()
