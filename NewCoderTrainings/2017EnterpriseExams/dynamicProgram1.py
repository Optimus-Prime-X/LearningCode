import sys

if __name__ == '__main__':
    while True:
        n = sys.stdin.readline()[:-1]
        if n == '':
            break
        n = int(n)
        ability = [int(c) for c in sys.stdin.readline()[:-1].split()]
        k, d = [int(c) for c in sys.stdin.readline()[:-1].split()]
        dp1 = [[0] * (k + 1) for _ in range(n+1)]
        dp2 = [[0] * (k + 1) for _ in range(n+1)]
        for i in range(1,n+1):
            dp1[i][1] = ability[i-1]
            dp2[i][1] = ability[i-1]
        for i in range(1,n+1):
            for j in range(1, k + 1):
                start = max(k - 1, i - d)
                tmp1 = dp1[i][j]
                tmp2 = dp2[i][j]
                while start < i:
                    dp1[i][j] = max(dp1[start][j - 1] * ability[i-1], dp2[start][j - 1] * ability[i-1], dp1[i][j])
                    dp2[i][j] = min(dp1[start][j - 1] * ability[i-1], dp2[start][j - 1] * ability[i-1], dp2[i][j])

                    start += 1
        print(max([num[k] for num in dp1]))