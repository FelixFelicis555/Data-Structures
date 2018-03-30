n = int(input("Enter no of vertices:"))
e = int(input("Enter no of edges:"))
# l = [[] for _ in range(n)]
l = [[0 for _ in range(n)] for _ in range(n)]
for i in range(e):
    u, v = map(int, input().split())
    l[u][v] = 1
    l[v][u] = 1
#PRINT ADJACENCY MATRIX
print("ADJACENCY MATRIX")
for j in range(n):
    for k in range(n):
        print(l[j][k],' ',end="")
    print("")