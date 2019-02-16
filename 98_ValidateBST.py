# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        import math
        if not root:
            return True
        def validate(node,lessthan,largerthan):
            if not node:
                return True
            if node.val>=lessthan or node.val<=largerthan:
                return False
            else:
                return(validate(node.left,min(lessthan,node.val),largerthan) and validate(node.right,lessthan,max(largerthan,node.val)))
        return validate(root,float('inf'),float('-inf'))
        """
        :type root: TreeNode
        :rtype: bool 
        """
        