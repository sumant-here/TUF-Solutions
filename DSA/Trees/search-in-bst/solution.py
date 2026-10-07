# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def searchBST(self, root, val):
        #your code goes here
        if root is None:
            return None 
        if root.data == val:
            return root 
        if val < root.data:
            return self.searchBST(root.left,val)
        else:
            return self.searchBST(root.right,val)
