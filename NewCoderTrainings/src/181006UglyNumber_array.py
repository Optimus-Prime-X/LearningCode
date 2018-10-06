# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        p2, p3, p5 = 0, 0, 0
        res = [1]
        if index == 1:
            return 1
        if index <= 0:
            return 0
        for i in range(1, index):
            newUgly = min(res[p2] * 2, res[p3] * 3, res[p5] * 5)
            res.append(newUgly)
            if newUgly == res[p2] * 2: p2 += 1
            if newUgly == res[p3] * 3: p3 += 1
            if newUgly == res[p5] * 5: p5 += 1
        return res[index]
