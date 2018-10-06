# -*- coding:utf-8 -*-
#分治法策略，原问题的解为两部分的解与穿越两部分的子数组中最大的
class Solution1:
    def __init__(self):
        self.neginfinity = -2 ** 31
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        left = 0
        right = len(array) - 1
        if len(array) <= 0:
            return 0
        elif len(array) == 1:
            return array[0]
        else:
            return self.FindLargestSubArray(array,left,right)
    def FindLargestSubArray(self, array, left, right):
        mid = (left + right) // 2
        if left == right:
            return array[left]
        else:
            return max(self.FindLargestSubArray(array, left, mid),
                self.FindLargestSubArray(array, mid + 1, right),
                self.FindCrossMaxSumSubArray(array, left, right, mid))
    def FindCrossMaxSumSubArray(self, array, left, right, mid):
        sumleft, sumright = self.neginfinity, self.neginfinity
        curr_sum = 0
        for i in range(mid, left - 1, -1):
            curr_sum += array[i]
            if curr_sum > sumleft:
                sumleft = curr_sum
        curr_sum = 0
        for i in range(mid + 1, right + 1):
            curr_sum += array[i]
            if curr_sum > sumright:
                sumright = curr_sum
        return sumright + sumleft

#动态规划法:定义res[i]保存以数i为末尾的最大子数组
class Solution2:
    def FindGreatestSumOfSubArray(self, array):
        res = [-1000000] * len(array)
        res[0] = array[0]
        for i in range(1,len(array)):
            res[i] = max(res[i - 1] + array[i], array[i])
        return max(res)


if __name__ == '__main__':
    s = Solution2()
    print(s.FindGreatestSumOfSubArray([6,-3,-2,7,-15,1,2,2]))