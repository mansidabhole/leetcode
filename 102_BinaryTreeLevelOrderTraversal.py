# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
 
class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        output=[]
        dummy=[]
        l=[]
        q=[root]
        while(len(q)>0):
            l=[root.val for root in q]
            dummy=[]
            output.append(l)
            for i,root in enumerate(q):
                dummy.append(root.left)
                dummy.append(root.right)
            q=[]
            q=[node for node in dummy if node]
        return output
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """