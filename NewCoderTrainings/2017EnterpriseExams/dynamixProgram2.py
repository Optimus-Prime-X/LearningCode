# 牛牛和 15 个朋友来玩打土豪分田地的游戏，牛牛决定让你来分田地，地主的田地可以看成是一个矩形，每个位置有一个价值。
# 分割田地的方法是横竖各切三刀，分成 16 份，作为领导干部，牛牛总是会选择其中总价值最小的一份田地,作为牛牛最好的朋友，
# 你希望牛牛取得的田地的价值和尽可能大，你知道这个值最大可以是多少吗？
# 思路：定义cal函数计算矩形的sum，所求值一定是取自[0,sum]之间，令其为k，可以判断是否存在一个划分使得k可以是最小的那个田地，
# 操作上使用暴力法，对矩阵纵向遍历划分，然后贪心的寻找每列中面积大于k的矩形数，如果大于等于4，则存在这样的划分满足取k，
# 找到最大的k即可，可以用二分查找

def cal(x1, y1, x2, y2, matSum):
    res = matSum[x2][y2] - matSum[x1][y2] - matSum[x2][y1] + matSum[x1][y1]
    return res


def check(k, matSum, n, m):
    for i1 in range(1, n - 2):
        if cal(0, 0, i1, m, matSum) < 4 * k: continue
        for i2 in range(i1 + 1, n - 1):
            if cal(i1, 0, i2, m, matSum) < 4 * k: continue
            for i3 in range(i2 + 1, n):
                if cal(i2, 0, i3, m, matSum) < 4 * k or cal(i3, 0, n, m, matSum) < 4 * k: continue
                count = 0
                start = 0
                for j in range(start + 1, m + 1):
                    s1 = cal(0, start, i1, j, matSum)
                    s2 = cal(i1, start, i2, j, matSum)
                    s3 = cal(i2, start, i3, j, matSum)
                    s4 = cal(i3, start, n, j, matSum)
                    if s1 >= k and s2 >= k and s3 >= k and s4 >= k:
                        count += 1
                        start = j
                if count >= 4:
                    return True
    return False


import sys

if __name__ == '__main__':
    while True:
        line = sys.stdin.readline()[:-1]
        if line == '':
            break
        n, m = [int(k) for k in line.split()]
        mat = [[] for _ in range(n)]
        matSum = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            mat[i] = [int(c) for c in sys.stdin.readline()[:-1]]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                matSum[i][j] = matSum[i][j - 1] + matSum[i - 1][j] - matSum[i - 1][j - 1] + mat[i - 1][j - 1]
        sumMax = matSum[n][m]
        start = 0
        end = matSum[n][m]
        k = k = (start + end) // 2
        maxk = 0
        while start < end:
            if check(k, matSum, n, m):
                if maxk < k:
                    maxk = k
                start = k + 1
                k = (start + end) // 2
            else:
                end = k
                k = (start + end) // 2
        print(maxk)
