class AdjacencyMatrix:
    def __init__(self, n):
        self.matrix = [[0 for _ in range(n)] for _ in range(n)]

    def add_edge(self, v1, v2):
        self.matrix[v1][v2] = 1
        self.matrix[v2][v1] = 1

    def display(self):
        for row in self.matrix:
            print(row)


class AdjacencyList:
    def __init__(self, n):
        self.list = [[] for _ in range(n)]

    def add_edge(self, v1, v2):
        self.list[v1].append(v2)
        self.list[v2].append(v1)

    def display(self):
        for index, v in enumerate(self.list):
            print('Vertex {}:'.format(index), end=' ')
            print(v)


def main():
    n = int(input('Enter number of vertices: '))
    print('Enter the edges: (x to stop)')
    l = AdjacencyList(n)
    m = AdjacencyMatrix(n)
    while True:
        t = input().split()
        if t[0] == 'x':
            break
        v1, v2 = map(int, t)
        m.add_edge(v1, v2)
        l.add_edge(v1, v2)

    l.display()
    print()
    m.display()

if __name__ == '__main__':
    main()