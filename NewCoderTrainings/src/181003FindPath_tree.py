# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Tree:
    def __init__(self, sq):
        self.tree = [TreeNode(k) for k in sq]
        for i in range(len(sq) // 2):
            self.tree[i].left = self.tree[2 * i + 1]
            self.tree[i].right = self.tree[2 * i + 2]
class Solution:
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        elif not root.left and not root.right and root.val == expectNumber:
            return [[root.val]]
        left = self.FindPath(root.left, expectNumber - root.val)
        right = self.FindPath(root.right, expectNumber - root.val)
        res = []
        for i in left + right:
            res.append([root.val] + i)
        return res


if __name__ == "__main__":
    s = Solution()
    tree = Tree([10,5,12,4,7])
    print(s.FindPath(tree.tree[0],22))