# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
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
                    output.append(current.val)
                    predecessor.right=current
                    current=current.left
                else:
                    predecessor.right=None
                    current=current.right
        return output
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        
        """
        #iterative solution using stacks
        
        if not root:
            return []
        stack=[root]
        output=[]
        while(len(stack)>0):
            root=stack.pop()
            output.append(root.val)
            if root.right is not None:
                stack.append(root.right)
            if root.left is not None:
                stack.append(root.left)
        return output      
        
        """