# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.jpfloor = []
    def jumpFloor(self, number):
        if len(self.jpfloor) == 0:
            self.jpfloor = [0] * (number+1)
            self.jpfloor[0] = 1
        if self.jpfloor[number]:
            return self.jpfloor[number]
        else:
            for i in range(number):
                self.jpfloor[number] += self.jumpFloor(i)
            return self.jpfloor[number]

