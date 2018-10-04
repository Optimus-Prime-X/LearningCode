# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.resList = []
    def Permutation(self, ss):
        self.Find('',ss)
        return self.resList

    def Find(self, curr, sRest):
        if not sRest:
            if curr not in self.resList:
                self.resList.append(curr)
        for i,k in enumerate(sRest):
            if i < len(sRest) - 1:
                self.Find(curr + k, sRest[:i]+sRest[i+1:])
            else:
                self.Find(curr + k, sRest[:i])
