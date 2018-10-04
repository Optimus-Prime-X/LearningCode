# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if sequence == []:
            return False
        if len(sequence) == 1:
            return True
        root = sequence.pop()
        left_sq, right_sq = [], []
        i = 0
        while i < len(sequence) and sequence[i] < root:
            left_sq.append(sequence[i])
            i += 1
        while i < len(sequence) and sequence[i] > root:
            right_sq.append(sequence[i])
            i += 1

        if i != len(sequence):
            return False
        if left_sq == [] or right_sq == []:
            return self.VerifySquenceOfBST(left_sq) or self.VerifySquenceOfBST(right_sq)
        else:
            return self.VerifySquenceOfBST(left_sq) and self.VerifySquenceOfBST(right_sq)