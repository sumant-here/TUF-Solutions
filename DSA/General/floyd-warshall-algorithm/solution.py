class Solution:
    def shortestDistance(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == -1:
                    matrix[i][j] = 10**9
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    if matrix[i][via] != 10**8 and matrix[via][j] != 10**8:
                        matrix[i][j] = min(matrix[i][j],matrix[i][via]+matrix[via][j])
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == 10**9:
                    matrix[i][j] = -1
        return matrix
    