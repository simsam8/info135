# NOTE: Linear and sequential search are the same

def linear_search(arr: list, value):
    for n in arr:
        if n == value:
            return True
    return False

def sequential_search(arr, item):
    i = 0
    found = False
    while i < len(arr) and not found:
        if arr[i] == item:
            found = True
        else:
            i += 1
    return found

# NOTE: Binary search requires a sorted input list


def binary_search_iterative(arr, value):
    bot = 0
    top = len(arr) - 1
    mid = top // 2
    found = False
    while bot <= top and not found:
        mid = (top - bot) // 2
        if value == arr[mid]:
            found = True
        elif arr[mid] < value:
            bot = mid + 1
        else:
            top = mid - 1
    return found


def binary_search_recursive(arr, item, low, high):
    if low > high:
        return False
    mid = (low + high) // 2
    if item == arr[mid]:
        return True
    elif item < arr[mid]:
        return binary_search_recursive(arr, item, low, mid - 1)
    else:
        return binary_search_recursive(arr, item, mid + 1, high)


if __name__ == "__main__":
    test = [1, 2, 3, 4, 5, 6, 7, 8]
    print(linear_search(test, 4))
    print(sequential_search(test, 4))
    print(binary_search_iterative(test, 4))
    print(binary_search_recursive(test, 4, 0, len(test)-1))
