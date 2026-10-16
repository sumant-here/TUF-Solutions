class Solution:
    def ninjaTraining(self, matrix):
        n = len(matrix)
        if n == 0 :
            return 0 
        dp  = [[0]* 3 for _ in range(n)] 
        dp[0] = matrix [0][:]
        for i in range(1,n):
            for j in range(3):
                p = matrix[i][j]
                best = 0 
                for k in range(3):
                    if k != j :
                        best = max(best,dp[i-1][k])
                dp[i][j] = p + best
        return max(dp[n-1])