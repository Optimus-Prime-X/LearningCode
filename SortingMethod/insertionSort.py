import numpy as np
def insertionSort(lyst):
    n = len(lyst)
    for i in range(n):
        for j in range(i+1,n):
            if lyst[j] < lyst[i]:
                lyst[j], lyst[i] = lyst[i], lyst[j]
    return lyst

if __name__ == "__main__":
    a = np.random.randint(100,size = 10)
    print(a)
    print(insertionSort(a))
