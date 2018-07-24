class Solution(object):
    def print_matrix(self, m):
        for r in m:
            for i in r:
                print i,
            print

    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        # matrix = zip(*matrix)
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        self.print_matrix(matrix)
        for i, v in enumerate(matrix):
            # v = list(v)
            matrix[i] = v[::-1]
        self.print_matrix(matrix)

        # n = len(matrix)
        # for l in range(n / 2):
        #     r = n - 1 - l
        #     for p in range(l, r):
        #         q = n - 1 - p
        #         cache = matrix[l][p]
        #         matrix[l][p] = matrix[q][l]
        #         matrix[q][l] = matrix[r][q]
        #         matrix[r][q] = matrix[p][r]
        #         matrix[p][r] = cache

M = Solution()
M.rotate([[1,2,3],[1,2,3],[1,2,3]])