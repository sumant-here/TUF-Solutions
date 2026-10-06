class Solution:
    def unionArray(self, nums1, nums2):
        n = len(nums1)
        m = len(nums2)

        res = []
        i = 0
        j = 0

        while i < n and j < m:

            if nums1[i] < nums2[j]:
                if len(res) == 0 or res[-1] != nums1[i]:
                    res.append(nums1[i])
                i += 1

            elif nums1[i] > nums2[j]:
                if len(res) == 0 or res[-1] != nums2[j]:
                    res.append(nums2[j])
                j += 1

            else:
                # Both are equal
                if len(res) == 0 or res[-1] != nums1[i]:
                    res.append(nums1[i])

                i += 1
                j += 1

        while i < n:
            if len(res) == 0 or res[-1] != nums1[i]:
                res.append(nums1[i])
            i += 1

        while j < m:
            if len(res) == 0 or res[-1] != nums2[j]:
                res.append(nums2[j])
            j += 1

        return res
