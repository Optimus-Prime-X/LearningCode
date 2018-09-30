
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code her
        if pRoot1 == None or pRoot2 == None:
            return False
        elif self.isSubtree(pRoot1, pRoot2):
            return True
        else:
            return self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)

    def isSubtree(self, tree1, tree2):
        if tree2 == None:
            return True
        elif tree1 == None or tree1.val != tree2.val:
            return False
        else:
            return self.isSubtree(tree1.left, tree2.left) and self.isSubtree(tree1.right, tree2.right)
