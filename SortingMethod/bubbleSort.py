import numpy as np
def bubbleSort(lyst):
    for i in range(len(lyst)):
        for j in range(len(lyst)-i-1):
            if lyst[j] > lyst[j + 1]:
                lyst[j], lyst[j + 1] = lyst[j + 1], lyst[j]
    return lyst

if __name__ == '__main__':
    a = np.random.randint(100,size = 10)
    print(a)
    print(bubbleSort(a))