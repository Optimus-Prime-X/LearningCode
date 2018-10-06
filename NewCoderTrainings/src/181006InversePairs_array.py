# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.res = 0

    def InversePairs(self, data):
        return self.CountInversePairs(data, 0, len(data) - 1) % 1000000007

    # write code here
    def CountInversePairs(self, data, left, right):
        if left == right:
            return 0
        mid = (left + right) // 2
        if left == mid:
            if data[left] > data[right]:
                data[left], data[right] = data[right], data[left]
                return 1
            else:
                return 0
        leftCount = self.CountInversePairs(data, left, mid) % 1000000007
        rightCount = self.CountInversePairs(data, mid + 1, right) % 1000000007
        currCount = leftCount + rightCount
        p1, p2 = mid, right
        currData = []
        while p1 >= left and p2 >= mid + 1:
            if data[p1] > data[p2]:
                currCount += p2 - mid
                currData.append(data[p1])
                p1 -= 1

            else:
                currData.append(data[p2])
                p2 -= 1
        for i in range(p1, left-1, -1):
            currData.append(data[i])
        for i in range(p2, mid, -1):
            currData.append(data[i])
        currData = currData[::-1]
        for i in range(left,right+1):
            data[i] = currData[i-left]
        return currCount


if __name__ == '__main__':
    s = Solution()
    print(s.InversePairs([364,637,341,406,747,995,234,971,571,219,993,407,416,366,315,301,601,650,418,355,460,505,360,965,516,648,727,667,465,849,455,181,486,149,588,233,144,174,557,67,746,550,474,162,268,142,463,221,882,576,604,739,288,569,256,936,275,401,497,82,935,983,583,523,697,478,147,795,380,973,958,115,773,870,259,655,446,863,735,784,3,671,433,630,425,930,64,266,235,187,284,665,874,80,45,848,38,811,267,575]))
