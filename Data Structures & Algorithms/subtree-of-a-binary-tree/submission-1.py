# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfsSearch(root, subRoot):
            if not subRoot:
                return True
            if not root:
                return False
            if dfsSame(root, subRoot):
                return True
            return dfsSearch(root.left, subRoot) or dfsSearch(root.right, subRoot)
            

        def dfsSame(root, subRoot):
            if not root and not subRoot:
                return True
            if root and subRoot and root.val == subRoot.val:
                return dfsSame(root.left, subRoot.left) and dfsSame(root.right, subRoot.right)
            return False

        return dfsSearch(root, subRoot)