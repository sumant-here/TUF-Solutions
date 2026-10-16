
class Solution:
    def frogJump(self, heights, k):
        n = len(heights)

        if n <= 1:
            return 0

        dp = [float('inf')] * n
        dp[0] = 0

        for i in range(1, n):
            for j in range(1, k + 1):
                if i - j >= 0:
                    cost = dp[i - j] + abs(
                        heights[i] - heights[i - j]
                    )
                    dp[i] = min(dp[i], cost)

        return dp[n - 1]
