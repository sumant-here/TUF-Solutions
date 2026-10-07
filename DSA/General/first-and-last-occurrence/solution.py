class Solution:
    def searchRange(self, nums, target):
        f = - 1
        l = 0 
        h = len(nums) -1
        while l <= h :
            mid = (l+h) // 2
            if nums[mid] == target:
                f = mid
                h = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                h = mid -1 
        ls = - 1
        l = 0 
        h = len(nums) -1
        while l <= h :
            mid = (l+h) // 2
            if nums[mid] == target:
                ls = mid
                l = mid + 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                h = mid -1 
        return [f,ls]


