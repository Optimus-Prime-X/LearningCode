def selectionSort(lyst):
    for i in range(len(lyst)):
        for j in range(i,len(lyst)):
            if lyst[j] < lyst[i]:
                lyst[j], lyst[i] = lyst[i], lyst[j]
    return lyst
if __name__ == '__main__':
    a = [2,5,1,6,4,8,7,3]
    print(selectionSort(a))