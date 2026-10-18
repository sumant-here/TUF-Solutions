class Solution:
    def perfectSum(self, arr, K):
        n = len(arr)
        dp = [[False]*(K+1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True
        if arr[0] <= K:
            dp[0][arr[0]] = True
        for i in range(1,n):
            for s in range(1,K+1):
                nt = dp[i-1][s]
                t = False
                if arr[i]<= s:
                    t = dp[i-1][s-arr[i]]
                dp[i][s] = nt + t 
        return dp[n-1][K] %(10**9+7)

     
