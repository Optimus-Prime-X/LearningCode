# -*- coding:utf-8 -*-
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        num = 1
        curr = head
        while curr.next != None:
            curr = curr.next
            num += 1
        for i in range(num - k):
            head = head.next
        return head.val

if __name__ == "__main__":
    line = input()
    ls = [int(k) for k in line.split()]
    k = int(input())
    head = ListNode(ls[0])
    curr = head
    for i in range(1, len(ls)):
        curr.next = ListNode(ls[i])
        curr = curr.next

    s = Solution()
    print(s.FindKthToTail(head, k))