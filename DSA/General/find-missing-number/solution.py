class Solution:
    def missingNumber(self, nums):
        n = len(nums) 
        s = (n*(n+1))/2
        t_s = sum(nums)
        return int(s - t_s)

        