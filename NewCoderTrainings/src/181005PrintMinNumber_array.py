# -*- coding:utf-8 -*-
#思路:
#1. 首先选择numbers集中首位数字最小的集合min_lastset，保存该最小数字为min_last
#2. 判断min_lastset中含有第二位的数字集合中，第二位数的最小数字min_curr,
#3. 需要做判断:1）当min_curr > min_last时，选择min_lastset中最小数作为输出；
#             2）当min_curr == min_last时，递归选择min_lastset中含有第三位的数字集合，第三位数的最小设为min_curr重做第3步
#             3）当min_curr < min_last时，按照1的规则选择min_lastset中第二位数字最小的集合，重新生成min_lastset，递归下去
class Solution:
    def __init__(self):
        self.numbers = []
        self.res = ''
    def PrintMinNumber(self, numbers):
        # write code here
        if not numbers:
            return ''
        self.numbers = numbers
        while self.numbers:
            numbers_s = [str(num) for num in self.numbers]
            min_curr = min([int(num[0]) for num in numbers_s if len(num) > 0])
            min_set = [num for num in numbers_s if len(num) > 0 and int(num[0]) == min_curr]
            self.PopCurrMin(min_curr, 1, min_set)
        return int(self.res)

    def PopCurrMin(self, min_last, k, min_lastset):
        min_curr = min([int(num[k]) for num in min_lastset if len(num) > k] or [min_last])
        min_set = [num for num in min_lastset if len(num) > k and int(num[k]) == min_curr]
        if min_curr < min_last and min_set:
            self.PopCurrMin(min_curr, k + 1, min_set)
        elif min_curr == min_last and min_set:
            self.PopCurrMin(min_curr, k + 1, min_lastset)
        else:
            popnum = min([int(num) for num in min_lastset])
            self.res += str(popnum)
            self.numbers.pop(self.numbers.index(popnum))

#自定义比较器
from functools import cmp_to_key
class Solution2:
    def  PrintMinNumber(self, numbers):
        numbers_s = [str(num) for num in numbers]
        cmp_key = cmp_to_key(lambda x, y: int(x + y) - int(y + x))
        numbers_s = sorted(numbers_s, key = cmp_key)
        return ''.join(numbers_s)

if __name__ == '__main__':
    s = Solution2()
    print(s.PrintMinNumber([3,32,321,320]))