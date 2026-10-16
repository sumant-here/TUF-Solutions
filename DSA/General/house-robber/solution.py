
class Solution:
    def houseRobber(self, money):
        n = len(money)
        if n == 0 :
            return 0 
        if n == 1:
            return money[0]
        def rob(arr):
            n = len(arr)
            if n == 1 :
                return arr[0]
            dp = [-1] * n 
            dp[0] = arr[0] 
            dp[1] = max(arr[0],arr[1])
            for i in range(2,n):
                p = arr[i] + dp[i-2]
                np = dp[i-1]
                dp[i] = max(p,np)
            return dp[n-1]
        case1 = rob(money[:-1])
        case2 = rob(money[1:])
        return max(case1,case2)
 