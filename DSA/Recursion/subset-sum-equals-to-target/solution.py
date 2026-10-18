class Solution:
    def isSubsetSum(self, arr, target):
        n = len(arr)
        dp = [[False]*(target+1) for _ in range(n)]
        for i in range(n):

            dp[i][0] = True
        if arr[0] <= target:
            dp[0][arr[0]] = True 
        for i in range(1,n):
            for s in range(1,target+1):
                nt = dp[i-1][s]
                t = False
                if arr[i] <= s :
                    t = dp[i-1][s-arr[i]]
                dp[i][s] = t or nt
        return dp[n-1][target]

     