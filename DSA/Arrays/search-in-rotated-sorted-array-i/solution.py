class Solution:
    def search(self, nums, k):
        l = 0 
        h = len(nums) -1 
        while l <= h :
            mid = (l +h) // 2
            if nums[mid] == k :
                return mid
            if nums[l] <= nums[mid]:
                if nums[l] <= k < nums[mid]:
                    h = mid -1
                else:
                    l = mid + 1
            else:
                if nums[mid] < k <=nums[h]:
                    l = mid + 1
                else:
                    h = mid - 1
        return -1

        

