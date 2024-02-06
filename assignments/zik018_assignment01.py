import math

# Task 1


def binary_search_big_o(iterator):
    n_elements = len(iterator)
    big_o = math.ceil(math.log2(n_elements))
    print(f"binary search with {n_elements} elements takes {big_o} steps")


italian_words = range(102400)
french_words = range(480000)

print("\nTask 1:\n")

print("a) Italian dictionary:", end=" ")
binary_search_big_o(italian_words)
print("b) French dictionary:", end=" ")
binary_search_big_o(french_words)


# Task 2


class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def get_data(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, data):
        if self.is_empty():
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next_node = self.head
            self.head = new_node

    def print_list(self):
        print("[", end="")
        current_node = self.head
        while current_node is not None:
            print(current_node.get_data(), end=", ")
            current_node = current_node.next_node
        print("]")


print("\nTask 2:\n")

ls = LinkedList()
ls.push(5)
ls.push(68)
ls.push(8)
ls.print_list()


# Task 3


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
        else:
            return self.items.pop()


def reverse_list(ls: list):
    stack = Stack()
    for item in ls:
        stack.push(item)

    reverse = []
    while True:
        item = stack.pop()
        if item is None:
            break
        reverse.append(item)

    print(reverse)


print("\nTask 3:\n")
ls = [1, 2, 3, 4, 5]
print(f"Input: {ls}")
print("Reverse: ", end="")

reverse_list(ls)
