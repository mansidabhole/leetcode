# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        if not head:
            return
        ptr1=head
        ptr2=head
        count=0
        while (count<n and ptr2 is not None):
            ptr2=ptr2.next
            count+=1
        if ptr2 is None:
            return head.next
        while(ptr2.next is not None):
            ptr1=ptr1.next
            ptr2=ptr2.next
        dummy=ptr1.next
        if dummy is None or dummy.next is None:
            ptr1.next=None
            return head
        else:
            ptr1.next=dummy.next
            return head
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        