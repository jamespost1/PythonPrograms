# CSCI 220/620
# Summer 2022
# Assignment 5 - Empirical Performance of Sorting Algorithms
# James Post
import random
import math
import time
import pandas as pd
import matplotlib.pyplot as plt


def pseudo_random_list(size):
    rl = [0]
    for i in range(1, size):
        rl.append(rl[i - 1] + random.randint(1, 10))
    random.shuffle(rl)
    return rl


def print_list(arr, indexes):
    s = ""
    for i in range(len(arr)):
        s += "*" if i in indexes else " "
        s += str(arr[i]) + " "
    print(s)


def is_sorted(arr, n):
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


def native_sort(arr, n, verbose=True):
    arr.sort()


# from https://www.geeksforgeeks.org/bubble-sort/
def bubble_sort(arr, n, verbose=True):
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                if verbose:
                    print_list(arr, [j, j+1])


# from https://www.geeksforgeeks.org/selection-sort/
def selection_sort(arr, n, verbose=True):
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        if verbose:
            print_list(arr, [i, min_idx])


# from https://www.geeksforgeeks.org/insertion-sort/
def insertion_sort(arr, n, verbose=True):
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        if verbose:
            print_list(arr, [i, j+1])


# from https://www.geeksforgeeks.org/cocktail-sort/
def cocktail_sort(arr, n, verbose):
    swapped = True
    start = 0
    end = n - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end = end - 1
        for i in range(end - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        start = start + 1
        if verbose:
            print_list(arr, [start, end])


# from https://www.geeksforgeeks.org/shellsort/
def shell_sort(arr, n, verbose):
    gap = int(n / 2)
    while gap > 0:
        j = gap
        while j < n:
            i = j - gap
            while i >= 0:
                if arr[i + gap] > arr[i]:
                    break
                else:
                    arr[i + gap], arr[i] = arr[i], arr[i + gap]
                i = i - gap
            j += 1
            if verbose:
                print_list(arr, [i, j])
        gap = int(gap / 2)


# from https://www.geeksforgeeks.org/merge-sort/
def merge_sort(arr, n, verbose):
    if n > 1:
        mid = int(n / 2)
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L, len(L), verbose)
        merge_sort(R, len(R), verbose)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# from https://www.geeksforgeeks.org/quick-sort/
def qs_partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# from https://www.geeksforgeeks.org/quick-sort/
def quick_sort_rec(arr, low, high, verbose):
    if low < high:
        pi = qs_partition(arr, low, high)
        quick_sort_rec(arr, low, pi - 1, verbose)
        quick_sort_rec(arr, pi + 1, high, verbose)
        if verbose:
            print_list(arr, [low, pi, high])


def quick_sort(arr, n, verbose):
    quick_sort_rec(arr, 0, n-1, verbose)


# from https://www.geeksforgeeks.org/heap-sort/
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[largest] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # swap
        heapify(arr, n, largest)


# from https://www.geeksforgeeks.org/heap-sort/
def heap_sort(arr, n, verbose):
    for i in range(int(n / 2 - 1), -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
        if verbose:
            print_list(arr, [i, 0])


def plot_times(dict_sorts, sorts, trials, sizes):
    sort_num = 0
    plt.xticks([j for j in range(len(sizes))], [str(size) for size in sizes])
    for sort_alg in sorts:
        sort_num += 1
        d = dict_sorts[sort_alg.__name__]
        x_axis = [j + .05 * sort_num for j in range(len(sizes))]
        y_axis = [d[i] for i in sizes]  # time
        plt.bar(x_axis, y_axis, width=.05, alpha=.75, label=sort_alg.__name__)
    plt.legend()
    plt.title("Runtime of Sorting Algorithms")
    plt.xlabel("Number of Elements")
    plt.ylabel("Time for " + str(trials) + " trials (ms)")
    plt.savefig("Assignment5.png")
    plt.show()


def main():
    sorts = [native_sort, bubble_sort, selection_sort, insertion_sort, cocktail_sort, shell_sort, merge_sort,
             quick_sort, heap_sort]
    dict_sorts = {}
    for sort_alg in sorts:
        dict_sorts[sort_alg.__name__] = {}
    trials = 1
    sizes = [100 * i for i in range(1, 11)]
    for size in sizes:
        for sort_alg in sorts:
            dict_sorts[sort_alg.__name__][size] = 0
        for trial in range(1, trials + 1):
            arr = pseudo_random_list(size)
            for sort_alg in sorts:
                arr_copy = arr.copy()
                start_time = time.time()
                sort_alg(arr_copy, size, verbose=False)
                end_time = time.time()
                net_time = end_time - start_time
                dict_sorts[sort_alg.__name__][size] += 1000 * net_time
                if not is_sorted(arr_copy, size):
                    print("Error in sort", sort_alg.__name__, size)
    pd.set_option("display.max_rows", 500)
    pd.set_option("display.max_columns", 500)
    pd.set_option("display.width", 1000)
    df = pd.DataFrame.from_dict(dict_sorts).T
    print(df)
    plot_times(dict_sorts, sorts, trials, sizes)


if __name__ == "__main__":
    main()
