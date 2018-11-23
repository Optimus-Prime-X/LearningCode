# 每个皇后的横坐标和纵坐标不能相同，因此可以设置一个list，其长度为n，且每个元素各不相同，代表不同的皇后
# 如Queen[i] = j代表皇后在（i，j）坐标
# 同时皇后与皇后之间应满足x1 - y1 != x2- y2 and x1 + y1 != x2 + y2
# 因此可以再设置两个list分别保存xi- yi 和xi+ yi的结果，每次判断第i行的n个皇后是否可以添加时，需要同时判断是否满足不在这三个list的条件

class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []
        def DFS(queens, qsub, qsum, count):
            count += 1
            p = len(queens)  # 代表新的一行，需要判断这行中n个皇后的
            if p == n:
                result.append(queens)
                return
            for q in range(n):
                if q not in queens and (p - q) not in qsub and (p + q) not in qsum:
                    DFS(queens + [q], qsub + [p - q], qsum + [p + q], count)
        DFS([],[],[],0)
        return [['.'*col + 'Q' +'.'*(n-col-1) for col in queens] for queens in result]
if __name__ == '__main__':
    s = Solution()
    print(s.solveNQueens(4))