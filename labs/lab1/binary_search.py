import math

# Exercise 1

a = [1, 3, 5, 7, 9, 13, 19, 21, 25]  # sorted
b = [5, 3, 7, 9, 0, 1, 4, 3, 5]  # not sorted
c = [2000, 1996, 1994, 1989, 1969, 1952, 1945]  # sorted from highest
d = ["A", "B", "C", "G", "E", "H", "I", "J", "K"]  # not sorted
e = ["ANTMAN", "BATMAN", "BEAST BOY", "CATWOMAN", "HAWKGIRL"]  # sorted

# A)
# Can use binary search on all of the above if we sort them
# For string based lists, we have to use string comparison

# B)


def test(low, high):
    print('low + high')
    print((low + high) // 2)
    print('other')
    print(low + (high - low) // 2)


# test(0, 10)
# test(10, 20)


def binary_search_iterative(array, low, high, x):
    while low <= high:
        mid = low + (high - low) // 2
        print(f"low: {low}, mid: {mid}, high: {high}")
        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1


def binary_search_recursive(array, low, high, x):
    if high >= low:
        mid = low + (high - low) // 2
        print(f"low: {low}, mid: {mid}, high: {high}")
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            return binary_search_recursive(array, mid + 1, high, x)
        else:
            return binary_search_recursive(array, low, mid - 1, x)

    else:
        return -1


# print(binary_search_iterative(a, 0, len(a) - 1, 13))
# print(binary_search_recursive(a, 0, len(a) - 1, 13))
print(binary_search_iterative(range(7), 0, 6, 0))


# Exercise 2


def binary_search_big_o(iterator):
    n_elements = len(iterator)
    big_o = math.ceil(math.log2(n_elements))
    print("Binary search")
    print(f"Number of steps: {big_o}")


def simple_search_big_o(iterator):
    print("Simple search")
    print(f"Number of steps: {len(iterator)}")


long_list = range(102400)
#
# binary_search_big_o(a)
# simple_search_big_o(a)
