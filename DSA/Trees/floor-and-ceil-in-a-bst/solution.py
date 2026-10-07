# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.data = val
#         self.left = left
#         self.right = right

class Solution:
    def floorCeilOfBST(self, root, key):
        #your code goes here
        flr = -1
        ceil = -1
        while root:
            if root.data == key:
                return [root.data,root.data]
            elif root.data < key:
                flr = root.data
                root = root.right
            else:
                ceil = root.data
                root = root.left
        return [flr,ceil] 