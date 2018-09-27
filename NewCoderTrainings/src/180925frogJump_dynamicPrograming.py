# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.jpfloor = []
    def jumpFloor(self, number):
        if len(self.jpfloor) == 0:
            self.jpfloor = [0] * (number+1)
            self.jpfloor[0] = 1
            self.jpfloor[1] = 1
        if self.jpfloor[number]:
            return self.jpfloor[number]
        else:
            self.jpfloor[number] =  self.jumpFloor(number - 1) + self.jumpFloor(number - 2)
            return self.jpfloor[number]

if __name__ == '__main__':
    solution = Solution()
    print(solution.jumpFloor(4))