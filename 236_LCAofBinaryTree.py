# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        from collections import deque
        def pathtonode(node,target):
            if node is None:
                return 
            if node.val==target:
                stack=deque()
                stack.appendleft(node)
                return stack
            leftpath=pathtonode(node.left,target)
            if leftpath:
                leftpath.appendleft(node.left)
                return leftpath
            rightpath=pathtonode(node.right,target)
            if rightpath:
                rightpath.appendleft(node.right)
                return rightpath
            return 
        if not root:
            return 
        pathp=pathtonode(root,p.val)
        pathq=pathtonode(root,q.val)
        res=root
        while(pathp is not None and pathq is not None):
            p=pathp.popleft()
            q=pathq.popleft()
            if p==q:
                res=p
            else:
                return res
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        