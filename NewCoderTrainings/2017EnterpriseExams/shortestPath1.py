WHITE, GRAY, BLACK = 0, 1, 2


def BFS(dis, color, map, n, m, move, startX, startY):
    queue = [[startX, startY]]
    dis[startX][startY] = 0
    color[startX][startY] = GRAY
    while queue:
        startX, startY = queue.pop(0)
        for dx, dy in move:
            targetX, targetY = startX + dx, startY + dy
            if 0 <= targetX < n and 0 <= targetY < m and map[targetX][targetY] != 'X' and color[targetX][
                targetY] == WHITE:
                color[targetX][targetY] = GRAY
                dis[targetX][targetY] = dis[startX][startY] + 1
                queue.append([targetX, targetY])
        color[startX][startY] = BLACK
    return dis


if __name__ == '__main__':
    import sys

    while True:
        line = sys.stdin.readline()[:-1]
        if line == '':
            break
        n, m = [int(k) for k in line.split()]
        map = [[] for _ in range(n)]
        for i in range(n):
            map[i] = [char for char in sys.stdin.readline()[:-1]]
        dis = [[-1] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if map[i][j] == 'X':
                    dis[i][j] = -2
        color = [[WHITE] * m for _ in range(n)]
        startX, startY = [int(k) for k in sys.stdin.readline()[:-1].split()]
        k = int(sys.stdin.readline()[:-1])
        move = []
        for i in range(k):
            move.append([int(k) for k in sys.stdin.readline()[:-1].split()])
        dis = BFS(dis, color, map, n, m, move, startX, startY)
        flag = True
        for i in range(n):
            for j in range(m):
                if dis[i][j] == -1:
                    flag = False
        if flag:
            max = max([max(line) for line in dis])
        else:
            max = -1
        print(max)

