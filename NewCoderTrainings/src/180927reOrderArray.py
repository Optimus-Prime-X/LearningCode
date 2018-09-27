# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        odd, even = [], []
        for k in array:
            if k % 2 == 1:
                odd.append(k)
            else:
                even.append(k)
        return odd + even