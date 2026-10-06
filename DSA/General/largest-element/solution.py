class Solution:
    def largestElement(self, nums):
        lar = nums[0]
        n = len(nums)
        for i in range(1,n):
            if nums[i] > lar:
                lar = nums[i]
        return lar
        