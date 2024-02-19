import time


def time_test_wrapper(sort_func, list_of_lists):
    """
    Check how a sorting algorithm performs on different lists.
    Parameters:
    sort_func (function): Sorting function to test
    list_ (list(list)): List of lists.
    e.g. [ [1,2,3], [3,4,5], [6,7,8,9] ]
    """
    for i, list_ in enumerate(list_of_lists):
        print(
            f"{sort_func.__name__} applied on --> List#{i}: length: {len(list_)}",
            end=" ",
        )
        time = time_sorting_algorithm(sort_func, list_)
        print("Time elapsed:", time)


def time_sorting_algorithm(sort_func, list_):
    """
    Measure the time taken by a sorting algorithm to sort a list.
    Parameters:
    sort_func (function): Sorting function to test.
    list_ (list): List to sort.
    Returns:
    float: time it took to sort the list
    """
    start_time = time.time()
    sorted_list = sort_func(list_)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


if __name__ == "__main__":
    # Example usage:
    input_array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    time_taken = time_sorting_algorithm(bubble_sort, input_array)
    print("Time taken for sorting:", time_taken, "seconds")
    # Example of testing multiple
    test_lists = [
        [i for i in range(10)],
        [i for i in range(10**2)],
        [i for i in range(10**3)],
        [i for i in range(10**4)],
    ]
    time_test_wrapper(bubble_sort, test_lists)
