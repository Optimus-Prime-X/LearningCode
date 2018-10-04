# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root :
            return []
        curr_queue = [root]
        next_queue = []
        res = []
        while len(curr_queue):
            curr_node = curr_queue.pop(0)
            res.append(curr_node.val)
            next_queue += [k for k in [curr_node.left, curr_node.right] if k]
            if not curr_queue and next_queue:
                curr_queue = next_queue
                next_queue = []
            elif not curr_queue and not next_queue:
                break
        return res
