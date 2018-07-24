# class Solution(object):
#     def solveNQueens(self, n):
#         """
#         :type n: int
#         :rtype: List[List[str]]
#         """
#         output = [["."] * n] * n
#         for i in range(n):
#             for j in range(n):
#                 if self.isvalid(output, i, j):
#                     print(i,j,output)
#                     output[i][j] = "Q"
#                     break
#         solution = []
#         for i in range(n):
#             solution.append("".join(output[i]))
#         return solution
#
#     def isvalid(self, M, i, j):
#         # if i == 0:
#         #     return True
#         for row in range(i - 1):
#             for col in range(len(M)):
#                 if M[row][col] == "Q" and i - row == abs(j - col):
#                     return False
#                 elif M[row][col] == "Q" and j == col:
#                     return False
#         return True

class Solution(object):

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        output = [["." for i in range(n)] for j in range(n)]
        self.sol = []
        self.findsol(0, 0, output, 0)
        return self.sol

    def findsol(self, i, j, matrix2, count):
        n = len(matrix2)
        print(i, j, matrix2)
        if i >= n:
            return
        matrix = [[matrix2[k][l] for k in range(n)] for l in range(n)]
        if self.isvalid(matrix, i, j):
            matrix[i][j] = "Q"
            count += 1
            if i == len(matrix) - 1:
                if count == len(matrix):
                    self.sol.append(matrix)
                return
            self.findsol(i + 1, 0, matrix, count)

        if j == len(matrix) - 1:
            self.findsol(i + 1, 0, matrix, count)
        else:
            self.findsol(i, j + 1, matrix, count)

    def isvalid(self, M, i, j):
        if i == 0:
            return True
        for row in range(i):
            for col in range(len(M)):
                if M[row][col] == "Q" and i - row == abs(j - col):
                    return False
                elif M[row][col] == "Q" and j == col:
                    return False
        return True


N = Solution()
print(N.solveNQueens(4))
