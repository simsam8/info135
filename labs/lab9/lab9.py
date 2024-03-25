# Exercise 1

# a) Pre-order: D, A, E, H, C, B, G, F
# b) In-order: H, A, D, E, C, B, G, F
# c) Post-order: D, E, A, G, F, B, C, H

# Exercise 2


class BinaryTree:
    def __init__(self, value) -> None:
        self.value = value
        self.left_child: BinaryTree | None = None
        self.right_child: BinaryTree | None = None

    def insert_left(self, value):
        if self.left_child is None:
            self.left_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.left_child = self.left_child
            self.left_child = new_node

    def insert_right(self, value):
        if self.right_child is None:
            self.right_child = BinaryTree(value)
        else:
            new_node = BinaryTree(value)
            new_node.right_child = self.right_child
            self.right_child = new_node

    def print_tree(self, level=0):
        print(" " * level * 2 + str(self.value))
        if self.left_child is not None:
            self.left_child.print_tree(level + 1)
        if self.right_child is not None:
            self.right_child.print_tree(level + 1)


def build_my_tree():
    tree = BinaryTree("H")
    tree.insert_left("A")
    tree.left_child.insert_left("D")
    tree.left_child.insert_right("E")
    tree.insert_right("C")
    tree.right_child.insert_right("B")
    tree.right_child.right_child.insert_left("G")
    tree.right_child.right_child.insert_right("F")

    tree.print_tree()


# Exercise 3


class BinarySearchTree:
    def __init__(self, value=None) -> None:
        self.value = value
        if self.value is not None:
            self.left_child = BinarySearchTree()
            self.right_child = BinarySearchTree()
        else:
            self.left_child = None
            self.right_child = None

    def is_empty(self):
        return self.value is None

    def insert(self, value):
        if self.is_empty():
            self.value = value
            self.left_child = BinarySearchTree()
            self.right_child = BinarySearchTree()
        elif value < self.value:
            self.left_child.insert(value)
        elif value > self.value:
            self.right_child.insert(value)

    def in_order(self):
        if self.is_empty():
            return []
        else:
            return (
                self.left_child.in_order() + [self.value] + self.right_child.in_order()
            )

    def print_tree(self):
        if not self.is_empty():
            print(self.in_order())


def find_max_and_min():
    tree = BinarySearchTree("H")
    tree.insert("A")
    tree.left_child.insert("D")
    tree.left_child.insert("E")
    tree.insert("C")
    tree.right_child.insert("B")
    tree.right_child.right_child.insert("G")
    tree.right_child.right_child.insert("F")

    ordered = tree.in_order()
    lowest, highest = ordered[0], ordered[-1]
    print(f"{lowest=}, {highest=}")


# Exercise 4

# Big O notation of: f(n) = 9n^4 + log_2(n^2 * 3) + 8n
# It has a BigO of n^4 as it is the highest term


if __name__ == "__main__":
    build_my_tree()
    find_max_and_min()
