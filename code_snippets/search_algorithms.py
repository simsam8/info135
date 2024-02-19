def linear_search(arr: list, value) -> int:
    """
    Returns position of found value, -1 if not found.
    """
    for i, n in enumerate(arr):
        if n == value:
            return i
    return -1


def binary_search(arr, value) -> int:
    """
    Input must be sorted.
    Returns position of found value, -1 if not found.
    """
    bot = 0
    top = len(arr)
    mid = top // 2
    while bot <= top:
        mid = (top - bot) // 2
        if value == arr[mid]:
            return mid
        elif arr[mid] < value:
            bot = mid + 1
        else:
            top = mid - 1
    return -1


if __name__ == "__main__":
    test = [1, 2, 3, 4, 5, 6, 7, 8]
    print(linear_search(test, 2))
    print(binary_search(test, 1))
