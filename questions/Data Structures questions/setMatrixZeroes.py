def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    """
            T(n) = o(n*n)
            s(n) = o(n)
        """

    row = len(matrix)
    col = len(matrix[0])

    zeroth_row = [False] * row
    zeroth_col = [False] * col

    for i in range(row):
        for j in range(col):
            if matrix[i][j] == 0:
                zeroth_row[i] = True
                zeroth_col[j] = True

    for i in range(row):
        for j in range(col):
            if zeroth_row[i] or zeroth_col[j]:
                matrix[i][j] = 0

    return matrix
