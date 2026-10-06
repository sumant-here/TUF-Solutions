class Solution:
    def longestConsecutive(self, nums):
        st = set(nums)
        ans = 0 
        for num in st:
            if num - 1 not in st:
                count = 1
                while num + count in st:
                    count += 1
                ans = max(ans,count)
        return ans 