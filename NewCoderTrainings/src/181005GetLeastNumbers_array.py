# -*- coding:utf-8 -*-
#用partition的思想进行处理，partition是快速排序的核心步骤，重点掌握
class Solution1:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if k > len(tinput) or k <= 0:
            return []
        left, right = 0, len(tinput) - 1
        pivotindex = self.Partition(tinput, left, right)
        while pivotindex != k - 1:
            if pivotindex < k-1:
                left = pivotindex + 1
                pivotindex = self.Partition(tinput, left, right)
            elif pivotindex > k-1:
                right = pivotindex - 1
                pivotindex = self.Partition(tinput, left, right)
        return sorted(tinput[:k])


    def Partition(self, array, left, right):
        pivot = array[right]
        pivotindex = left - 1
        for i in range(left,right + 1):
            if array[i] < pivot:
                pivotindex += 1
                array[i], array[pivotindex] = array[pivotindex], array[i]
        array[right] = array[pivotindex + 1]
        array[pivotindex + 1] = pivot
        return pivotindex + 1

#最小堆的方式
class Solution2:
    def GetLeastNumbers_Solution(self, tinput, k):
        if k <= 0 or k > len(tinput):
            return []
        minList = tinput[:k]
        for i in range(k // 2,-1,-1):
            self.max_heap(minList,i)
        for i in range(k,len(tinput)):
            if tinput[i] < minList[0]:
                minList[0] = tinput[i]
                self.max_heap(minList, 0)
        return sorted(minList)

    def max_heap(self, A, i):
        left = 2 * i + 1
        right = 2 * i + 2
        if left >= len(A) and right >= len(A):
            return
        if left < len(A) and A[i] < A[left]:
            largest = left
        else:
            largest = i
        if right < len(A) and A[right] > A[largest]:
            largest = right
        if largest != i:
            A[i], A[largest] = A[largest], A[i]
            self.max_heap(A, largest)




if __name__ == '__main__':
    s = Solution2()
    print(s.GetLeastNumbers_Solution([4,5,1,6,2,7,3,8],4))