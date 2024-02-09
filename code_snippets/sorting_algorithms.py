from copy import copy


def selection_sort(arr: list) -> list:
    for i in range(len(arr)):
        low_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[low_idx]:
                low_idx = j

        arr[i], arr[low_idx] = arr[low_idx], arr[i]

    return arr


def bubble_sort(arr: list) -> list:
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
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


def merge_sort(arr: list) -> list:
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr


def quick_sort(arr: list) -> list:
    if len(arr) < 2:
        return arr

    pivot = arr[0]
    left = [i for i in arr[1:] if i <= pivot]
    right = [i for i in arr[1:] if i > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


sortable_lists = [[3, 2, 1], [8, 6, 7, 4, 2, 6, 8], [], [1, 2, 3]]
for l in sortable_lists:
    print("Input list: ", l)
    print("Bubble Sort: ", bubble_sort(copy(l)))
    print("Selection Sort: ", selection_sort(copy(l)))
    print("Insertion Sort: ", insertion_sort(copy(l)))
    print("Merge Sort: ", merge_sort(copy(l)))
    print("Quick Sort: ", quick_sort(copy(l)))
    print()
