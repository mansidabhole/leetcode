# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        def findsum(root, sum):
            if root.left is not None:
                if findsum(root.left,sum-root.val):
                    return True
            if root.right is not None:
                if findsum(root.right,sum-root.val):
                    return True
            if root.left is None and root.right is None and root.val==sum:
                return True
            else:
                return False
        if not root:
            return False
        return findsum(root, sum)
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        