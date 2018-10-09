import sys
if __name__ == '__main__':
    while True:
        n = sys.stdin.readline()[:-1]
        if n == '':
            break
        n = int(n)
        apple = [int(k) for k in sys.stdin.readline()[:-1].split()]
        sumApple = sum(apple)
        average = sumApple // n
        if average * n != sumApple:
            print(-1)
        else:
            dic = {}
            flag = 1
            for i in range(n):
                di = apple[i] - average
                if di % 2 == 1:
                    print(-1)
                    flag = 0
                    break
                if di not in dic:
                    dic[di] = 0
                dic[di] += 1
            if flag:
                sumPos = sum([dic[k] * k for k in dic.keys() if k > 0])
                sumNeg = sum([dic[k] * k for k in dic.keys() if k < 0])
                if sumPos + sumNeg != 0:
                    print(-1)
                else:
                    print(sumPos // 2)