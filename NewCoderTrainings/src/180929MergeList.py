# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        rHead = ListNode(-1)
        curr = rHead
        while pHead1 != None and pHead2 != None:
            if pHead1.val > pHead2.val:
                curr.next = pHead2
                pHead2 = pHead2.next
            else:
                curr.next = pHead1
                pHead1 = pHead1.next
            curr = curr.next
        if pHead1:
            curr.next = pHead1
        elif pHead2:
            curr.next = pHead2
        return rHead.next