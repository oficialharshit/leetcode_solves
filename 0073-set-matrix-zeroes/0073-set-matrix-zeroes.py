class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix[0]) # cols
        n = len(matrix) # rows
        col = [0]*m
        row = [0]*n
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    col[j]=1
                    row[i]=1
        for i in range(n):
            for j in range(m):
                if col[j] == 1 or row[i] ==1 :
                    matrix[i][j]=0