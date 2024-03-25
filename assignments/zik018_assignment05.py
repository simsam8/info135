# Task 1
# All of the binary trees are full, i.e. all the interior nodes have two children.


# Task 2

# Matrix ii displays the adjacency matrix of the graph


# Task 3


def binary_tree(r):
    return [r, [], []]


def get_left_child(root):
    return root[1]


def get_right_child(root):
    return root[2]


def insert_left_child(root, new_branch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [new_branch, t, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root


def insert_right_child(root, new_branch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [new_branch, t, []])
    else:
        root.insert(2, [new_branch, [], []])
    return root


def make_tree():
    print("\nTask 3")
    my_tree = binary_tree(1)
    insert_left_child(my_tree, 2)
    insert_right_child(my_tree, 3)

    insert_left_child(get_left_child(my_tree), 4)
    insert_left_child(get_right_child(my_tree), 5)
    insert_right_child(get_right_child(my_tree), 6)

    print(my_tree)


# Task 4


class Graph:
    def __init__(self) -> None:
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, from_vertex, to_vertex):
        if from_vertex not in self.graph:
            self.graph[from_vertex] = []
        self.graph[from_vertex].append(to_vertex)
        if to_vertex not in self.graph:
            self.add_vertex(to_vertex)

    def print_graph(self):
        for vertex, edges in self.graph.items():
            print(vertex + ": " + str(edges))

    def dfs(self, start):
        visited = []
        stack = [start]

        while stack:
            vertex = stack.pop()
            visited.append(vertex)
            for x in self.graph.get(vertex, []):
                if x not in visited:
                    stack.append(x)
        return visited


def build_my_graph2():
    print("\nTask 4")
    print("Create the graph")
    graph = Graph()
    graph.add_edge("b", "a")
    graph.add_edge("a", "c")
    graph.add_edge("c", "b")
    graph.add_edge("a", "d")
    graph.add_edge("d", "e")
    graph.add_edge("e", "a")
    graph.print_graph()

    print("Ouput from DFS")
    visited = graph.dfs("b")
    print(visited)


# Task 5


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

    def compute_sum(self) -> int:
        if self.is_empty():
            return 0
        else:
            return (
                self.left_child.compute_sum()
                + self.value
                + self.right_child.compute_sum()
            )

    def compute_count(self):
        if self.is_empty():
            return 0
        else:
            return (
                self.left_child.compute_count() + 1 + self.right_child.compute_count()
            )


def task5():
    print("\nTask 5")
    my_tree = BinarySearchTree()
    my_tree.insert(2)
    my_tree.insert(4)
    my_tree.insert(6)
    my_tree.insert(8)
    my_tree.insert(10)
    my_tree.insert(12)

    print(f"sum: {my_tree.compute_sum()}")
    print(f"number of nodes: {my_tree.compute_count()}")


if __name__ == "__main__":
    make_tree()
    build_my_graph2()
    task5()
