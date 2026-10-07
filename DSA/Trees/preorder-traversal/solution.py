# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data= val
#         self.left = left
#         self.right = right

class Solution:
    def preorder(self, root):
        #your code goes here
        ans = []
        def solve(node):
            if node is None:
                return
            ans.append(node.data)
            solve(node.left)
            solve(node.right)
        solve(root)
        return ans