# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root == None:
            return None
        self.Swap(root)
        return root
    def Swap(self, root):
        if root.right == None and root.left == None:
            return
        elif root.right and root.left == None:
            root.right, root.left = root.left, root.right
            self.Swap(root.left)
        elif root.right == None and root.left:
            root.right, root.left = root.left, root.right
            self.Swap(root.right)
        else :
            root.right, root.left = root.left, root.right
            self.Swap(root.left)
            self.Swap(root.right)