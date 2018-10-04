# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:

    def LastNode(self, pHead, lastNode):
        if not pHead:
            return
        pcurr = pHead
        if pcurr.left:
            leftLastNode = self.LastNode(pcurr.left)
        if lastNode:
            lastNode.right = pHead
            pHead.left = lastNode
        lastNode = pcurr
        if pcurr.right:
            lastNode = self.LastNode(pcurr.right)
        return lastNode

    def Convert(self, pRootOfTree):
        # write code here
        pLastNode = self.LastNode(pRootOfTree)
        pcurr = pLastNode
        while pcurr and pcurr.left:
            pcurr = pcurr.left
        return pcurr