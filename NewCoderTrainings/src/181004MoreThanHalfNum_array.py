# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0
        dic = {}
        for n in numbers:
            if str(n) not in dic:
                dic[str(n)] = 0
            dic[str(n)] += 1
        maxnum = max(dic.values())
        if maxnum < len(numbers) // 2 + 1:
            return 0
        else:
            return int([k for k in dic.keys() if dic[k] == maxnum][0])

if __name__ == '__main__':
    s = Solution()
    print(s.MoreThanHalfNum_Solution([1,4,3,2,4,4,5,4,2,4,4,4,4,4,4,4,4,5,4,4,7,4,4,0,4,4]))