class Solution:
    def countOccurrences(self, arr, target):
        # Your code goes here
        f = - 1
        l = 0 
        h = len(arr) - 1
        while l <= h :
            mid = (l+h) // 2
            if arr[mid] == target:
                f = mid
                h = mid-1
            elif arr[mid] < target:
                l = mid + 1
            else:
                h = mid - 1
        ls = - 1
        l = 0 
        h = len(arr) - 1
        while l <= h :
            mid = (l+h) // 2
            if arr[mid] == target:
                ls = mid
                l = mid+1
            elif arr[mid] < target:
                l = mid + 1
            else:
                h = mid - 1
        if f == -1 :
            return 0 
        return ls - f + 1
        