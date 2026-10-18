class Solution:
    def minDifference(self, arr, n):
        tot = sum(arr)
        dp = [[False]*(tot+1) for _ in range(n)]
        for i in range(n):
            dp[i][0] = True 
        if arr[0] <= tot:
            dp[0][arr[0]] = True
        for i in range(1,n):
            for s in range(1,tot+1):
                nt = dp[i-1][s]
                t = False
                if arr[i] <= s:
                    t = dp[i-1][s-arr[i]]
                dp[i][s] = t or nt
        mini = float('inf')

        for s in range(tot // 2 + 1):
            if dp[n - 1][s]:
                mini = min(mini, tot - 2 * s)
        return mini

    
