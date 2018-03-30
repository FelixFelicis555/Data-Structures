from bfs import Queue
from bfs import Graph


class DirectedGraph(Graph):
    def add_edge(self, v1, v2):
        self.list[v1].append(v2)

    def detect_cycles(self):
        visited = []
        q = Queue()
        q.enqueue(0)
        visited.append(0)
        while not q.is_empty():
            v = q.dequeue()
            for neighbour in self.list[v]:
                if neighbour not in visited:
                    q.enqueue(neighbour)
                    visited.append(neighbour)
                else:
                    return True
        return False


def main():
    n = 4
    d = DirectedGraph(n)
    d.add_edge(0, 1)
    d.add_edge(1, 2)
    d.add_edge(2, 3)
    d.add_edge(3, 3)
    # d.add_edge(3, 0)
    print(d.detect_cycles())


if __name__ == '__main__':
    main()