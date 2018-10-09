class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        res = []
        if tsum <= 1:
            return res
        for i in range(2,int((2*tsum)**0.5)+1):
            a1 = tsum / i -(i - 1)/2
            ak = tsum/i + (i-1)/2
            if a1 % 1 == 0 and ak % 1 == 0:
                res.append(list(range(int(a1),int(ak)+1)))
        res.sort(key=lambda x:x[0])
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.FindContinuousSequence(2000))