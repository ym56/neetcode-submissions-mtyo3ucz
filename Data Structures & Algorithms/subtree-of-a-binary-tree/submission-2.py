# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True

        def search(root):
            if not root:
                return False
            if same(root, subRoot):
                return True
            return search(root.left) or search(root.right)


        def same(l, r):
            if not l and not r:
                return True
            if l and r and l.val == r.val:
                return same(l.left, r.left) and same(l.right, r.right)
            return False

        return search(root)