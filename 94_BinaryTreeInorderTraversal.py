# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        if not root:
            return []
        output=[]
        stack=[root]
        while(len(stack)>0):
            root=stack[-1]
            if root.right is not None:
                root=stack.pop()
                stack.append(root.right)
                stack.append(root)
                root.right=None
            if root.left is not None:
                stack.append(root.left)
                root.left=None
                continue
            else:
                root=stack.pop()
                output.append(root.val) 
        return output
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        """
        #using morris traversal
        def findPredecessor(root):
            current=root.left
            while(current.right!=None and current.right!=root):
                current=current.right
            return current
        output=[]
        current=root
        while(current!=None):
            if current.left==None:
                output.append(current.val)
                current=current.right
            else:
                predecessor=findPredecessor(current)
                if predecessor.right==None:
                    predecessor.right=current
                    current=current.left
                else:
                    predecessor.right=None
                    output.append(current.val)
                    current=current.right
        return output
        """
        