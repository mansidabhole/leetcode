# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        if not head:
            return None
        prev=head.next
        head.next=None
        while(prev is not None):
            curr=prev.next
            prev.next=head
            head=prev
            prev=curr
        return head
        """
        :type head: ListNode
        :rtype: ListNode
        """
        