class Solution:
    def stockBuySell(self, arr, n):
        dp = [[[0]*3 for _ in range(2)]for _ in range(n+1)]
        for i in range(n-1,-1,-1):
            for buy in range(2):
                for cap in range(1,3): #at most 2 time so 1 2, 
                    if buy == 1:
                        dp[i][buy][cap] = max(-arr[i]+dp[i+1][0][cap],dp[i+1][1][cap])
                    else:
                        dp[i][buy][cap] = max(arr[i]+dp[i+1][1][cap-1],dp[i+1][0][cap])
        return dp[0][1][2]

