class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence or len(sequence) == 1:
            return True
        root = sequence.pop()
        i = 0
        left_sq, right_sq = [], []
        index = 0
        while i < len(sequence) and sequence[i] < root:
            left_sq.append(sequence[i])
            i += 1
        while i < len(sequence) and sequence[i] > root:
            right_sq.append(sequence[i])
            i += 1
        if i != len(sequence):
            return False
        elif i == len(sequence):
            return self.VerifySquenceOfBST(left_sq) and self.VerifySquenceOfBST(right_sq)

if __name__ == '__main__':
    s = Solution()
    print(s.VerifySquenceOfBST([4,8,6,12,16,14,10]))