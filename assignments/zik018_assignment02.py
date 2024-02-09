class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)


def selection_sort_3_passes():
    arr = [1502, 1560, 1600, 1540, 100, 1660, 1700, 2024]
    print("Before sorting:")
    print(arr)
    for i in range(3):
        low_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[low_idx]:
                low_idx = j

        arr[i], arr[low_idx] = arr[low_idx], arr[i]

    print("List after 3 passes:")
    print(arr)


def bubble_sort_3_passes():
    arr = [400, 10, 210, 160, 70, 220, 280, 380, 180, 260, 540]
    print("Before sorting:")
    print(arr)
    for i in range(3):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    print("List after 3 passes: ")
    print(arr)


def sort_and_rem_dump(arr):
    # Insertion sort
    for i in range(1, len(arr)):
        x = arr[i]
        j = i - 1
        while j >= 0 and x < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = x

    no_dupes = []
    for num in arr:
        if num in no_dupes:
            pass
        else:
            no_dupes.append(num)
    return no_dupes


def check_palindrome(word):
    my_stack = Stack()
    my_queue = Queue()
    for c in word:
        my_stack.push(c)
        my_queue.enqueue(c)

    for _ in range(len(word)):
        if my_stack.pop() != my_queue.dequeue():
            print(f"{word} is not a Palindrom")
            return
    print(f"{word} is a Palindrome")
    return


print("\nTask 1: selection_sort_3_passes")
selection_sort_3_passes()

print("\nTask 2: bubble_sort_3_passes")
bubble_sort_3_passes()

print("\nTask 3: sort and remove duplicates")
my_list = [3, 8, 9, 4, 0, 3, 8]
print("Before function: ", my_list)
my_list = sort_and_rem_dump(my_list)
print("After function: ", my_list)

print("\nTask 4: check if palindrome")
palin = "civic"
not_palin = "hello"

check_palindrome(palin)
check_palindrome(not_palin)
