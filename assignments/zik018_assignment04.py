# Task 1

# d) represents the edge set of the graph


# Task 2

# AB: 7 -> 1.
# AC: 13 -> 2.
# ABC: 22
# ABD: 16 -> 4.
# ACD: 14 -> 3.
# ACE: 24
# ACDE: 19 -> 5.
# ABDE: 21

# 1) ABCD with distance 19 is the chosen shortest path


# Task 3

COLUMNS = "abcde"
NUM_QUEENS = len(COLUMNS)
ACCEPT = 1
CONTINUE = 2
ABANDON = 3
all_solutions = []


def examine(partial_sol):
    for i in range(len(partial_sol)):
        for j in range(i + 1, len(partial_sol)):
            if attacks(partial_sol[i], partial_sol[j]):
                return ABANDON
    if len(partial_sol) == NUM_QUEENS:
        return ACCEPT
    else:
        return CONTINUE


def attacks(p1, p2):
    column1 = COLUMNS.index(p1[0]) + 1
    row1 = int(p1[1])

    column2 = COLUMNS.index(p2[0]) + 1
    row2 = int(p2[1])

    return (
        row1 == row2 or column1 == column2 or abs(row1 - row2) == abs(column1 - column2)
    )


def extend(partial_sol):
    results = []
    row = len(partial_sol) + 1

    for column in COLUMNS:
        new_solution = list(partial_sol)
        new_solution.append(column + str(row))
        results.append(new_solution)
    return results


def solve(partial_sol):
    exam = examine(partial_sol)
    if exam == ACCEPT:
        all_solutions.append(partial_sol)
    elif exam != ABANDON:
        for p in extend(partial_sol):
            solve(p)
    return all_solutions


def is_solution(candidate_solution):
    solve(candidate_solution)
    return candidate_solution in all_solutions


def task3():

    candidate_solution1 = ["d3", "c1", "e5", "b4", "a2"]
    candidate_solution2 = ["e4", "a1", "c5", "d2", "b1"]

    print("\nTask 3")
    print(is_solution(candidate_solution1))
    print(is_solution(candidate_solution2))


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

        if to_vertex not in self.graph:
            self.add_vertex(to_vertex)

        self.graph[from_vertex].append(to_vertex)

    def print_graph(self):
        for vertex, edges in self.graph.items():
            print(vertex + ": " + str(edges))

    def remove_vertex(self, vertex):
        for v, edges in self.graph.items():
            if vertex in edges:
                edges.pop(edges.index(v))

        del self.graph[vertex]


def task4():
    print("\nTask 4")
    graph = Graph()
    graph.add_edge("a", "b")
    graph.add_edge("a", "c")
    graph.add_edge("b", "c")
    graph.add_edge("b", "d")
    graph.add_edge("c", "d")
    graph.add_edge("d", "e")

    print("Before removal of vertex:")
    graph.print_graph()
    graph.remove_vertex("a")
    print("After removal of vertex:")
    graph.print_graph()


def main():
    task3()
    task4()


if __name__ == "__main__":
    main()
