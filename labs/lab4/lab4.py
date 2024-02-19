import math
from time_sorting_algorithms import *

# Exercise 1

n = 8464
print(f"{n*math.log2(n)=}")
print(f"{n**2=}")
print(f"{n=}")


# Exercise 2
def one_pass(liste, index):
    if index == len(liste):
        return liste
    sub_liste = liste[index:]
    smallest = min(sub_liste)
    smallest_index = sub_liste.index(smallest) + index
    liste[index], liste[smallest_index] = (liste[smallest_index], liste[index])

    return one_pass(liste, index + 1)


liste = [-4, 0, 1, 9, 0]
print(one_pass(liste, 0))


# Exercise 3


def selection_sort(arr: list) -> list:
    for i in range(len(arr)):
        low_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[low_idx]:
                low_idx = j

        arr[i], arr[low_idx] = arr[low_idx], arr[i]

    return arr


def insertion_sort(arr: list) -> list:
    for i in range(1, len(arr)):
        x = arr[i]
        j = i - 1
        while j >= 0 and x < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = x
    return arr


test_lists = [
    [i for i in range(10)],
    [i for i in range(10**2)],
    [i for i in range(10**3)],
    [i for i in range(10**4)],
]

time_test_wrapper(selection_sort, test_lists)
time_test_wrapper(insertion_sort, test_lists)

# Exercise 4



def partition(arr, low, high, pivot):
    i = low
    j = low
    while j < high:
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        elif arr[j] == pivot:
            arr[j], arr[high] = arr[high], arr[j]
            j -= 1
        j += 1

    arr[i], arr[high] = arr[high], arr[i]
    return i


def nut_and_bolt_match(nuts, bolts, low, high):
    if low < high:
        pivot = partition(nuts, low, high, bolts[high])
        partition(bolts, low, high, nuts[pivot])
        nut_and_bolt_match(nuts, bolts, low, pivot-1)
        nut_and_bolt_match(nuts, bolts, pivot + 1, high)


def match_nuts_and_bolts(nuts, bolts, low, high):
    print(nuts)
    print(bolts)
    nut_and_bolt_match(nuts, bolts, low, high)
    print(nuts)
    print(bolts)

nuts = ["@", "#", "$", "%", "^", "&"]
bolts = ["$", "%", "&", "^", "@", "#"]

match_nuts_and_bolts(nuts, bolts, 0, len(nuts)-1)
