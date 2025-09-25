class Solution(object):
    def setZeroes(self, matrix):
        rows, cols = len(matrix), len(matrix[0])
        colum_mark=[False]*cols
        row_mark=[False]*rows
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]==0:
                    row_mark[i]=True
                    colum_mark[j]=True
        for i in range(rows):
            for j in range(cols):
                if colum_mark[j] or row_mark[i]:
                    matrix[i][j]=0
        

        