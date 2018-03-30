from graph import AdjacencyList


class Queue:
    def __init__(self):
        self.elements = []

    def enqueue(self, x):
        self.elements.append(x)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.elements.pop(0)

    def is_empty(self):
        return len(self.elements) == 0


class Graph(AdjacencyList):

    def add_edge(self, v1, v2):
        self.list[v1].append([v2, None])
        self.list[v2].append([v1, None])

    def bfs(self, source):
        visited = []
        q = Queue()
        q.enqueue((source, 0))
        visited.append(source)
        while not q.is_empty():
            node = q.dequeue()
            v = node[0]
            d = node[1]
            for neighbour in self.list[v]:
                if neighbour[0] not in visited:
                    neighbour[1] = d + 1
                    q.enqueue(neighbour)
                    visited.append(neighbour[0])
            print("{}, Distance: {}".format(v, d))


def main():
    n = int(input('Enter number of vertices: '))
    l = Graph(n)
    print('Enter the edges: (x to stop)')
    while True:
        t = input().split()
        if t[0] == 'x':
            break
        v1, v2 = map(int, t)
        l.add_edge(v1, v2)
    s = int(input('Enter source vertex for BFS: '))
    l.bfs(s)


if __name__ == '__main__':
    main()
