class Solution:
    def minTriangleSum(self, triangle):
        n = len(triangle)
        dp = [[0]*n for _ in range(n)]
        dp[0][0] = triangle[0][0]
        for i in range(1,n):
            for j in range(i+1):
                up = float('inf')
                dig = float('inf')
                if i > j :
                    up = dp[i-1][j]
                if j > 0 :
                    dig = dp[i-1][j-1]
                dp[i][j]  = triangle[i][j]+ min(up,dig)
        return min(dp[n-1][:n])