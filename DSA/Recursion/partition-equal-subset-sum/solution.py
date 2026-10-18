class Solution:
    def equalPartition(self, n, arr):
        tot = sum(arr)
        if tot % 2 != 0 :
            return False
        tar = tot // 2
        dp = [[False]*(tar+1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True 
        if arr[0] <= tar:
            dp[0][arr[0]] = True
        for i in range(1,n):
            for s in range(1,tar+1):
                nt = dp[i-1][s]
                t = False
                if arr[i] <= s:
                    t = dp[i-1][s-arr[i]]
                dp[i][s] = t or nt
        return dp[n-1][tar]

    