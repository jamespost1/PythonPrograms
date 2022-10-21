# CSCI 220/620
# Summer 2022
# Assignment 4 - Empirical Performance of Search Algorithms
# James Post
import random
import math
import time
import pandas as pd
import matplotlib.pyplot as plt


def random_list(mn, mx, size, do_sorted, is_unique):
    rl = []
    i = 0
    while i < size:
        rn = random.randint(mn, mx)
        if is_unique and rn not in rl:
            rl.append(rn)
            i += 1
    if do_sorted:
        rl.sort()
    return rl


def pseudo_random_list(size):
    rl = [0]
    for i in range(1, size):
        rl.append(rl[i - 1] + random.randint(1, 10))
    return rl


def native_search(arr, key):
    return arr.index(key)


def linear_search(arr, key):
    for i in range(0, key):
        if arr[i] == key:
            return i
    return -1


def binary_search(arr, key):
    return bin_search_rec(arr, 0, len(arr) - 1, key)


def bin_search_rec(arr, l, r, key):
    if r >= l:
        mid = int(l + (r - l) / 2)
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return bin_search_rec(arr, l, mid - 1, key)
        else:
            return bin_search_rec(arr, mid + 1, r, key)
    else:
        return -1


def better_binary_search(arr, key):
    l = 0
    r = len(arr) - 1
    while r - l > 1:
        m = int(l + (r - l) / 2)
        if arr[m] <= key:
            l = m
        else:
            r = m
    if arr[l] == key:
        return l
    if arr[r] == key:
        return r
    else:
        return -1


def bin_search_random(arr, l, r, key):
    if r >= l:
        mid = random.randint(l, r)
        if arr[mid] == key:
            return mid
        if arr[mid] > key:
            return bin_search_random(arr, l, mid - 1, key)
        return bin_search_random(arr, mid + 1, r, key)
    return -1


def randomized_binary_search(arr, key):
    return bin_search_random(arr, 0, len(arr) - 1, key)


def exponential_search(arr, key):
    if arr[0] == key:
        return 0
    n = len(arr)
    i = 1
    while i < n and arr[i] <= key:
        i = i * 2
    return bin_search_rec(arr, int(i / 2), min(i, n - 1), key)


def interpolation_search_rec(arr, l, r, key):
    if l == r:
        if arr[l] == key:
            return l
        else:
            return -1
    if l <= r and arr[l] <= key <= arr[r]:
        pos = l + int(((r - l) / (arr[r] - arr[l])) * (key - arr[l]))
        if arr[pos] == key:
            return pos
        if arr[pos] < key:
            return interpolation_search_rec(arr, pos + 1, r, key)
        if arr[pos] > key:
            return interpolation_search_rec(arr, l, pos - 1, key)
    return -1


def interpolation_search(arr, key):
    return interpolation_search_rec(arr, 0, len(arr) - 1, key)


# from https://www.geeksforgeeks.org/jump-search/
def jump_search(arr, key):
    n = len(arr)
    step = math.sqrt(n)
    prev = 0
    while arr[int(min(step, n) - 1)] < key:
        prev = step
        step += math.sqrt(n)
        if prev >= n:
            return -1
    while arr[int(prev)] < key:
        prev += 1
        if prev == min(step, n):
            return -1
    if arr[int(prev)] == key:
        return int(prev)
    return -1


# from https://www.geeksforgeeks.org/fibonacci-search/
def fibonacci_search(arr, key):
    n = len(arr)
    fib_2 = 0
    fib_1 = 1
    fib_m = fib_2 + fib_1
    while fib_m < n:
        fib_2 = fib_1
        fib_1 = fib_m
        fib_m = fib_2 + fib_1
    offset = -1
    while fib_m > 1:
        i = min(offset + fib_2, n - 1)
        if arr[i] < key:
            fib_m = fib_1
            fib_1 = fib_2
            fib_2 = fib_m - fib_1
            offset = i
        elif arr[i] > key:
            fib_m = fib_2
            fib_1 = fib_1 - fib_2
            fib_2 = fib_m - fib_1
        else:
            return i
    if fib_1 and arr[n - 1] == key:
        return n - 1
    return -1


def plot_times(dict_searches, searches, trials, sizes):
    search_num = 0
    plt.xticks([j for j in range(len(sizes))], [str(size) for size in sizes])
    for search in searches:
        search_num += 1
        d = dict_searches[search.__name__]
        x_axis = [j + .05 * search_num for j in range(len(sizes))]
        y_axis = [d[i] for i in sizes]
        plt.bar(x_axis, y_axis, width=.05, alpha=.75, label=search.__name__)
    plt.legend()
    plt.title("Runtime of Search Algorithms")
    plt.xlabel("Size of data")
    plt.ylabel("Time for " + str(trials) + "Trials (ms)")
    plt.savefig("Assignment4.png")
    plt.show()


def main():
    searches = [native_search, linear_search, binary_search, better_binary_search, randomized_binary_search,
                exponential_search, interpolation_search, jump_search, fibonacci_search]
    dict_searches = {}
    for search in searches:
        dict_searches[search.__name__] = {}
    trials = 10
    sizes = [10000 * i for i in range(1, 11)]
    for size in sizes:
        for search in searches:
            dict_searches[search.__name__][size] = 0
        for trial in range(1, trials + 1):
            arr = pseudo_random_list(size)
            idx = random.randint(1, size) - 1
            key = arr[idx]
            for search in searches:
                start_time = time.time()
                idx_2 = search(arr, key)
                end_time = time.time()
                net_time = end_time - start_time
                dict_searches[search.__name__][size] += 1000 * net_time
                if idx != idx_2:
                    print("Error in search", search.__name__, size, idx, idx_2, key)
    pd.set_option("display.max_rows", 500)
    pd.set_option("display.max_columns", 500)
    pd.set_option("display.width", 1000)
    df = pd.DataFrame.from_dict(dict_searches).T
    print(df)
    plot_times(dict_searches, searches, trials, sizes)


if __name__ == "__main__":
    main()
