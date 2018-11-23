#有一片1000*1000的草地，小易初始站在(1,1)(最左上角的位置)。小易在每一秒会横向或者纵向移动到相邻的草地上吃草(小易不会走出边界)。
# 大反派超超想去捕捉可爱的小易，他手里有n个陷阱。第i个陷阱被安置在横坐标为xi ，纵坐标为yi 的位置上，小易一旦走入一个陷阱，将会被超超捕捉。
# 你为了去解救小易，需要知道小易最少多少秒可能会走入一个陷阱，从而提前解救小易。
import sys
def FindShortest():
    while True:
        n = sys.stdin.readline()[:-1]
        if n == '':
            break
        n = int(n)
        xSet = [int(c) for c in sys.stdin.readline()[:-1].split()]
        ySet = [int(c) for c in sys.stdin.readline()[:-1].split()]
        delta = [[1,0], [-1,0],[0,1],[0,-1]]
        WHITE, GRAY, BLACK = 0, 1, 2
        map = [[0] * 1001 for _ in range(1001)]
        for i in range(n):
            map[xSet[i]][ySet[i]] = 1
        color = [[0] * 1001 for _ in range(1001)]
        dis = [[-1] * 1001 for _ in range(1001)]
        dis[1][1], color[1][1] = 0, WHITE
        queue = [[1,1]]
        while queue:
            sX, sY = queue.pop(0)
            color[sX][sY] = GRAY
            for d in delta:
                sXc, sYc= sX + d[0], sY + d[1]
                if 0 < sXc <= 1000 and 0 < sYc <= 1000 and color[sXc][sYc] == WHITE:
                    queue.append([sXc, sYc])
                    dis[sXc][sYc] = dis[sX][sY] + 1
                    color[sXc][sYc] = GRAY
                if map[sXc][sYc] == 1:
                    return dis[sXc][sYc]
            color[sX][sY] = BLACK

if __name__ == '__main__':
    print(FindShortest())


