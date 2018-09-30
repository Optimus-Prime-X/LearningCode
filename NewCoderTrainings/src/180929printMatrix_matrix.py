class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        res = []
        if len(matrix[0]) == 1:
            return [k[0] for k in matrix]
        else:
            while matrix:
                res += matrix[0]
                matrix = matrix[1:]
                if matrix:
                    matrix = self.turn(matrix)
            return res
    def turn(self,matrix):
        mat = [[] for _ in range(len(matrix[0]))]
        for i in range(len(matrix[0])):
            mat[i] = [matrix[j][-i-1] for j in range(len(matrix))]
        return mat
if __name__ == '__main__':
    s = Solution()
    print(s.printMatrix([[1,2],[3,4]]))