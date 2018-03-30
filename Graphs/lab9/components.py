from graph import AdjacencyList
from bfs import Queue


class ComponentGraph(AdjacencyList):

    def component_of(self, i):
        visited = []
        q = Queue()
        q.enqueue(i)
        visited.append(i)
        while not q.is_empty():
            v = q.dequeue()
            for neighbour in self.list[v]:
                if neighbour not in visited:
                    q.enqueue(neighbour)
                    visited.append(neighbour)
        return visited

    def components(self):
        vertices = [i for i in range(len(self.list))]
        l = self.component_of(0)
        print(l)
        diff = list(set(vertices) - set(l))
        while len(diff) is not 0:
            k = self.component_of(diff[0])
            print(k)
            l += k
            diff = list(set(vertices) - set(l))


def main():
    n = 8
    d = ComponentGraph(n)
    d.add_edge(0, 1)
    d.add_edge(1, 2)
    d.add_edge(2, 3)
    d.add_edge(3, 3)
    d.add_edge(4, 5)
    d.add_edge(7, 6)
    d.components()


if __name__ == '__main__':
    main()