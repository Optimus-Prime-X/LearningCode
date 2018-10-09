# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def TreeDepth(self, pRoot):
        if pRoot == None:
            return 0
        return self.DFS(pRoot, 1)
        # write code here
    def DFS(self,currRoot, currDepth):
        if currRoot != None:
            return max(self.DFS(currRoot.left, currDepth + 1), self.DFS(currRoot.right, currDepth + 1))
        else:
            return currDepth