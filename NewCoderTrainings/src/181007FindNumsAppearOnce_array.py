# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        dic = {}
        for num in array:
            if num not in dic:
                dic[num] = 0
            dic[num] += 1
            if dic[num] == 2:
                dic[num] = 0
        res = []
        for k in dic.keys():
            if dic[k]:
                res.append(k)
        return res