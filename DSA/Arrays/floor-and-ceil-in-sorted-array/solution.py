class Solution:
    def getFloorAndCeil(self, nums, x):
        fl = -1
        cl = -1
        l = 0 
        h = len(nums) -1
        while l <= h:
            mid = (l+h)//2
            if nums[mid] ==x:
                return [x,x]
            elif nums[mid] < x:
                fl = nums[mid]
                l = mid +1
            else:
                cl = nums[mid]
                h = mid - 1
        return [fl,cl]
       
