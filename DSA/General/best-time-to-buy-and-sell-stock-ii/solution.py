class Solution:
    def stockBuySell(self, arr, n):
        dp = [[0]*2 for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            dp[i][1] = max(-arr[i]+dp[i+1][0],dp[i+1][1])
            dp[i][0] = max(arr[i]+dp[i+1][1],dp[i+1][0])
        return dp[0][1]

