# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        ptr1=headA
        ptr2=headB
        if ptr1==ptr2:
            return ptr1
        if headA is None or headB is None:
            return
        while(True):
            ptr1=ptr1.next
            ptr2=ptr2.next
            if ptr1 is None and ptr2 is None:
                return 
            if ptr1==None:
                ptr1=headB
            if ptr2==None:
                ptr2=headA
            if ptr1==ptr2:
                return ptr1      
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        
        
        