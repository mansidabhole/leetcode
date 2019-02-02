# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        if not root:
            return []
        output=[]
        stack=[root]
        while(len(stack)>0):
            root=stack[-1]
            if ((not root.right) and (not root.left)):
                root=stack.pop()
                output.append(root.val)
                continue
            if(root.right is not None):
                stack.append(root.right)
                root.right=None
            if(root.left is not None):
                stack.append(root.left)
                root.left=None
        return output
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        