# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        ls = []
        curr = pHead
        while curr != None:
            ls.append(curr)
            curr = curr.next
        rHead = ls.pop()
        curr = rHead
        while len(ls):
            curr.next = ls.pop()
        return rHead