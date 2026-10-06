class Solution:
    def rotateArray(self, nums, k: int) -> None:
        n= len(nums)
        k = k% n 
        # for _ in range(k):
        #     f = nums[0]
        #     for i in range(1,n):
        #         nums[i-1] = nums[i]
        #     nums[n-1] = f
        # return nums
        nums[:] = nums[k:] + nums[:k]
        return nums
