# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        res = 1
        if exponent > 0:
            for i in range(exponent):
                res *= base
            return res
        elif exponent < 0:
            for i in range(-1 * exponent):
                res *= 1 / base
            return res
        else:
            return 1