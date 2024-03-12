# Exercise 1

# 1) Graph is directed
# 2) False
# 3) True


# Exercise 2


class Graph:
    def __init__(self) -> None:
        self.graph = dict()

    def add_edge(self, node, neighbor):
        if node not in self.graph:
            self.graph[node] = [neighbor]
        else:
            self.graph[node].append(neighbor)

    def nodes_out_degree(self, n: int) -> list:
        out_nodes = []
        for node, neigbors in self.graph.items():
            if len(neigbors) == n:
                out_nodes.append(node)
        return out_nodes

    def print_graph(self):
        print(self.graph)

    # Exercise 3
    # a)
    def remove_edge(self, node1: str, node2: str):
        if node2 in self.graph[node1]:
            self.graph[node1].remove(node2)

    # b)
    def bfs(self, goal, root):
        queue = []
        explored = {root}
        queue.insert(0, root)
        while queue != []:
            current = queue.pop()
            if current == goal:
                return current
            for neighbor in self.graph[current]:
                if neighbor not in explored:
                    explored.add(neighbor)
                    queue.insert(0, neighbor)

        return None


if __name__ == "__main__":
    graph = Graph()
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "A")
    graph.add_edge("C", "A")
    graph.add_edge("C", "F")
    graph.add_edge("B", "C")
    graph.add_edge("F", "B")

    graph.print_graph()
    print(graph.nodes_out_degree(1))

    print(graph.graph["A"])
    graph.remove_edge("A", "B")
    print(graph.graph["A"])

    print(graph.bfs("F", "A"))
