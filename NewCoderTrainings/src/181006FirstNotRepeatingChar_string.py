# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if s == '':
            return -1
        dic = {}
        l = []
        dicIndex = {}
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = 0
                dicIndex[s[i]] = i
            dic[s[i]] += 1
        singleSet = [dicIndex[k] for k in dicIndex.keys() if dic[k] == 1]
        if singleSet:
            return min(singleSet)
        else:
            return -1