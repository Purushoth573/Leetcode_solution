class Solution(object):
    def setZeroes(self, matrix):
        rows, cols = len(matrix), len(matrix[0])

        # First pass: mark cells with -1 instead of directly making them 0
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    # Mark entire row
                    for k in range(cols):
                        if matrix[i][k] != 0:
                            matrix[i][k] = -1000
                    for k in range(rows):
                        if matrix[k][j] != 0:
                            matrix[k][j] = -1000

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == -1000:
                    matrix[i][j] = 0

        