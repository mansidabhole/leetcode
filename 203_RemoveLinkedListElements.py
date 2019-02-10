# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        while(True):
            if not head:
                return
            if head.val!= val:
                prev=head
                break
            else:
                head=head.next
        curr=head.next
        if curr is None:
            return head
        while(curr.next is not None):
            if curr.val==val:
                prev.next=curr.next
            else:
                prev=prev.next
            curr=curr.next
        if curr.next==None and curr.val==val:
            prev.next=None       
        return head
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        