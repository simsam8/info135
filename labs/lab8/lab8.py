from hashlib import md5

# Exercise 1

# A) not full, not perfect, not complete
# B) full, not perfect, complete
# C) full, perfect, complete


# Exercise 2
class BinaryTree:
    def __init__(self, value) -> None:
        self.value = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, value) -> None:
        if self.left_child is None:
            self.left_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.left_child = self.left_child
            self.left_child = new_node

    def insert_right(self, value) -> None:
        if self.right_child is None:
            self.right_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.right_child = self.right_child
            self.right_child = new_node

    def search(self, value) -> bool:
        if self.value == value:
            return True
        if self.left_child and self.left_child.search(value):
            return True
        if self.right_child and self.right_child.search(value):
            return True
        return False

    def print_tree(self, level=0) -> None:
        print(" " * level * 2 + str(self.value))
        if self.left_child is not None:
            self.left_child.print_tree(level + 1)
        if self.right_child is not None:
            self.right_child.print_tree(level + 1)


def exercise2() -> None:
    print("\nExercise 2")
    tree = BinaryTree("A")
    tree.insert_right("C")
    tree.insert_left("B")
    tree.left_child.insert_left("D")
    tree.left_child.insert_right("E")
    tree.print_tree()


# Exercise 3
def exercise3() -> None:
    print("\nExercise 3")
    door_id = "cyd"

    password = ""

    index = 0
    while len(password) < 4:
        to_hash = door_id + str(index)
        hex_string = md5(to_hash.encode()).hexdigest()
        if hex_string[0] == "0" and hex_string[1] == "0":
            password += hex_string[3]
        index += 1

    print(f"{password=}")


def main() -> None:
    exercise2()
    exercise3()


if __name__ == "__main__":
    main()
