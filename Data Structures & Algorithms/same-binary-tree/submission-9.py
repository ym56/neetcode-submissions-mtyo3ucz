# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not p and q) or (not q and p):
            return False
        if not p and not q:
            return True

        stackP = [p]
        stackQ = [q]
        while stackP or stackQ:
            if (not stackP) != (not stackQ):
                return False

            nodeP = stackP.pop()
            nodeQ = stackQ.pop()
            print(nodeP, nodeQ)
            if nodeP.val != nodeQ.val:
                return False

            if ((not nodeP.left) != (not nodeQ.left)) or ((not nodeP.right) != (not nodeQ.right)):
                return False

            if nodeP.left:
                stackP.append(nodeP.left)
                stackQ.append(nodeQ.left)

            if nodeP.right:
                stackP.append(nodeP.right)
                stackQ.append(nodeQ.right)
            
        return True