class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        rows, cols = len(matrix), len(matrix[0])

        cols_num = set()

        for i in range(rows):
            flag = False
            for j in range(cols):
                if matrix[i][j] == 0:
                    if flag == False:
                        flag = True
                        for k in range(0, j):
                            matrix[i][k] = 0
                        
                    if j not in cols_num:
                        cols_num.add(j)
                        for k in range(0, i):
                            matrix[k][j] = 0

                elif flag or j in cols_num:
                    matrix[i][j] = 0

        return