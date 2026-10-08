class Solution:
    def secondLargestElement(self, nums):
        n = len(nums)
        # if n < 2:
        #     return None 
        fir = float('-inf')
        sec = float('-inf')
        for i in range(n):
            if nums[i] > fir:
                sec = fir
                fir = nums[i]
            elif nums[i] > sec and nums[i] != fir  :
                sec = nums[i]
        if sec == float('-inf'):
            return -1
        return sec