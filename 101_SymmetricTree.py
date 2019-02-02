# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        def ismirror(root1,root2):
            if root1 is None and root2 is None:
                return True
            elif root1 is None or root2 is None:
                return False
            elif root1.val==root2.val:
                return (ismirror(root1.right,root2.left) and ismirror(root1.left,root2.right))
            else:
                return False
        if not root:
            return True
        else:
            return ismirror(root.left,root.right)
                
                
        
        """
        :type root: TreeNode
        :rtype: bool
        """