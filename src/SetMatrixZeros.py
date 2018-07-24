def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    h = len(matrix)
    if h == 0:
        return
    w = len(matrix[0])
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 0:
                for tmp in range(h):
                    if matrix[tmp][j] != 0:
                        matrix[tmp][j] = 'a'
                for tmp in range(w):
                    if matrix[i][tmp] != 0:
                        matrix[i][tmp] = 'a'
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 'a':
                matrix[i][j] = 0

matrix = [[1,1,1],[1,0,1],[1,1,1]]
setZeroes(matrix)
print matrix