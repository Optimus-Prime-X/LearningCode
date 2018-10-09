import sys


def FindOrderPairs(array, start, end):
    mid = (start + end) // 2
    if start == end:
        return 0
    if start == mid:
        if array[start] < array[end]:
            return 1
        else:
            array[start], array[end] = array[end], array[start]
            return 0
    leftCount = FindOrderPairs(array, start, mid)
    rightCount = FindOrderPairs(array, mid + 1, end)
    tmp = []
    count = leftCount + rightCount
    i, j = start, mid + 1
    while i <= mid and j <= end:
        if array[i] < array[j]:
            tmp.append(array[i])
            count += end - j + 1
            i += 1
        else:
            tmp.append(array[j])
            j += 1
    if i > mid:
        tmp += array[j:end + 1]
    else:
        tmp += array[i:mid + 1]
    array[start:end + 1] = tmp
    return count


def GenerateArray(indexEqZero, resNum, resArray, resSet, array):
    if not resSet and resNum >= len(indexEqZero):
        resArray.append(array[:])
        return
    else:
        index = indexEqZero[resNum - 1]
        for s in resSet:
            array[index] = s
            GenerateArray(indexEqZero[:resNum - 1], resNum - 1, resArray, resSet - {s}, array)


if __name__ == '__main__':
    while True:
        line = sys.stdin.readline()[:-1]
        if line == '':
            break
        n, k = [int(c) for c in line.split()]
        array = [int(c) for c in sys.stdin.readline()[:-1].split()]
        resSet = set(range(n + 1)) - set(array)
        if not resSet:
            print(FindOrderPairs(array, 0, n-1) == k and 1 or 0)
        else:
            resArray = []
            indexEqZero = [i for i in range(n) if array[i] == 0][::-1]
            GenerateArray(indexEqZero, len(resSet), resArray, resSet, array)
            print(len([1 for arrayi in resArray if FindOrderPairs(arrayi,0,n-1) == k] ))
