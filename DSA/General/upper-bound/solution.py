class Solution:
    def upperBound(self, nums, x):
        l = 0 
        h = len(nums) - 1
        ans = len(nums)
        while l <= h:
            mid =(l+h) // 2
            if x < nums[mid]:
                ans = mid
                h = mid -1
            else:
                l = mid + 1
        return ans
        
                
                
       


