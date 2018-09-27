# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.rect = []
    def rectCover(self, number):
        # write code here
        if number == 0:
            return 0
        if number == 1:
            return 1
        if number == 2:
            return 2
        if len(self.rect) == 0:
            self.rect = [0] * (number+1)
            self.rect[1], self.rect[2] = 1, 2
        if self.rect[number]:
            return self.rect[number]
        else:
            self.rect[number] = self.rectCover(number - 1) + self.rectCover(number - 2)
            return self.rect[number]