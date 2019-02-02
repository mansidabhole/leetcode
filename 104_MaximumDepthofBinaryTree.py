# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        def findDepth(root):
            if not root:
                return 0
            if (not root.left and not root.right):
                return 1
            else:
                return max((findDepth(root.right),findDepth(root.left)))+1
        return findDepth(root)
        """
        :type root: TreeNode
        :rtype: int
        """
        