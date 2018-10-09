# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        if pRoot == None:
            return True
        if abs(self.DFS(pRoot.left, 0) - self.DFS(pRoot.right, 0)) <= 1:
            return True
        else:
            return False
        # write code here
    def DFS(self,root,depth):
        if root == None:
            return depth
        return max(self.DFS(root.left, depth + 1),self.DFS(root.right, depth + 1))