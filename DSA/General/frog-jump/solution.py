class Solution:
    def frogJump(self, heights):
        n = len(heights)
        if n <= 1 :
            return 0
        dp = [0] * n 
        dp[1] = abs(heights[1]-heights[0])
        for i in range(2,n):

            ju_1 = dp[i-1] + abs(heights[i]-heights[i-1])
            ju_2 = dp[i-2] + abs(heights[i]- heights[i-2])
            dp[i] = min(ju_1,ju_2)
        return dp[n-1]
            
