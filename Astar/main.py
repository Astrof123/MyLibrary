class Node:
    def __init__(self, parent, g, h):
        self.parent = parent
        self.g = g
        self.h = h
        self.f = self.g + self.h


n, m = list(map(int, input().split()))
highs = []

for i in range(n):
    highs.append(list(map(int, input().split())))

print()

visited = [[0 for j in range(m)] for i in range(n)]
data = [[0 for j in range(m)] for i in range(n)]
places = [[0 for j in range(m)] for i in range(n)]

cord = list(map(int, input().split()))
places[cord[0]][cord[1]] = 1
start = Node(0, 0, 0)
data[cord[0]][cord[1]] = start
visited[cord[0]][cord[1]] = 1

cord = list(map(int, input().split()))
places[cord[0]][cord[1]] = 2
finish = [cord[0], cord[1]]

cord = list(map(int, input().split()))
places[cord[0]][cord[1]] = 3


destination = 2
vist = 0

while True:
    minum = 100000
    for i in range(n):
        for j in range(m):
            if visited[i][j] == 1 and data[i][j].f < minum:
                minum = data[i][j].f
                x = i
                y = j
    if places[x][y] == destination:
        if destination == 3:
            vist += data[x][y].f
            break
        vist += data[x][y].f
        visited = [[0 for j in range(m)] for i in range(n)]
        data = [[100 for j in range(m)] for i in range(n)]
        data[x][y] = Node(0, 0, 0)
        visited[x][y] = 1
        finish = cord
        destination = 3

    if x + 1 < n and visited[x + 1][y] == 0 and abs(highs[x][y] - highs[x + 1][y]) <= 100:
        data[x + 1][y] = Node(data[x + 1][y], data[x][y].g + 1, abs(x + 1 - finish[0]) + abs(y - finish[1]))
        visited[x + 1][y] = 1

    if x - 1 >= 0 and visited[x - 1][y] == 0 and abs(highs[x][y] - highs[x - 1][y]) <= 100:
        data[x - 1][y] = Node(data[x - 1][y], data[x][y].g + 1, abs(x - 1 - finish[0]) + abs(y - finish[1]))
        visited[x - 1][y] = 1

    if y + 1 < m and visited[x][y + 1] == 0 and abs(highs[x][y] - highs[x][y + 1]) <= 100:
        data[x][y + 1] = Node(data[x][y + 1], data[x][y].g + 1, abs(x - finish[0]) + abs(y + 1 - finish[1]))
        visited[x][y + 1] = 1

    if y - 1 >= 0 and visited[x][y - 1] == 0 and abs(highs[x][y] - highs[x][y - 1]) <= 100:
        data[x][y - 1] = Node(data[x][y - 1], data[x][y].g + 1, abs(x - finish[0]) + abs(y - 1 - finish[1]))
        visited[x][y - 1] = 1

    visited[x][y] = 2

print(vist)


