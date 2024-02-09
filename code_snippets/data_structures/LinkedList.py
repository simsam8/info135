class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        """Check if the linked list is empty"""
        return self.head is None

    def push(self, data):
        """Adds a new item to the beginning of the linked list"""
        if self.is_empty():
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node

    def append(self, data):
        """Adds a new item to the end of the linked list"""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next is not None:
                last_node = last_node.next
            last_node.next = new_node

    def search(self, data):
        """Checks if an item exists in the linked list"""
        current = self.head
        found = False
        while current and not found:
            if current.data == data:
                found = True
            else:
                current = current.next
        return found

    def size(self):
        """Returns the number of elements in the linked list"""
        if self.is_empty():
            return 0
        else:
            count = 1
            current = self.head
            while current.next is not None:
                count += 1
                current = current.next
            return count

    def pop(self):
        """Removes and returns the last item in the linked list"""
        if self.is_empty():
            return self.head
        else:
            prev = None
            current = self.head
            while current.next is not None:
                prev = current
                current = current.next
            if prev is None:
                self.head = None
            else:
                prev.next = None
            return current.data

    def print_list(self):
        """Print the list"""
        print("[", end="")
        current_node = self.head
        while current_node is not None:
            print(current_node.get_data(), end=", ")
            current_node = current_node.next
        print("]")


if __name__ == "__main__":
    my_list = LinkedList()
    my_list.push(6)
    my_list.push(6)
    my_list.print_list()
    print(my_list.size())
    last_value = my_list.pop()
    print(last_value)
    my_list.print_list()
    print(my_list.size())
