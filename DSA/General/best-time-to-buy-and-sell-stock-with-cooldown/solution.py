class Solution:
    def maxProfit(self, arr):
        # Your code goes here
        n = len(arr)
        dp = [[0]*2 for _ in range(n+2)]
        for i in range(n-1,-1,-1):
            for buy in range(2):
                if buy == 1:
                    dp[i][1] = max(-arr[i]+dp[i+1][0],dp[i+1][1])
                else:
                    dp[i][0] = max(arr[i]+dp[i+2][1],dp[i+1][0])
        return dp[0][1]
