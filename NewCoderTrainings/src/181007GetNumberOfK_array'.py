# -*- coding:utf-8 -*-
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        left = 0
        right = len(data) - 1
        mid = (left + right) // 2
        if len(data) == 0:
            return 0
        while k != data[mid] and left != mid:
            if k > data[mid]:
                left = mid
                mid = (left + right) // 2
            else:
                right = mid
                mid = (left + right) // 2
        if k != data[mid]:
            return 0
        lmid, rmid = mid, mid
        res = 0
        while lmid >= 0 and k == data[lmid]:
            res += 1
            lmid -= 1
        while rmid < len(data) and k == data[rmid]:
            res += 1
            rmid += 1
        return res - 1
if __name__ == '__main__':
    s = Solution()
    print(s.GetNumberOfK([1,1,2,3,4,4,4,5,6,7,7,7,8,10], 11))