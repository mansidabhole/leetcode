# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val <= l2.val:
            head=l1
            l1=l1.next
        else:
            head=l2
            l2=l2.next
        curr=head
        while (l1 is not None and l2 is not None):
            if(l1.val<=l2.val):
                curr.next=l1
                l1=l1.next
            else:
                curr.next=l2
                l2=l2.next
            curr=curr.next
        if l1 is not None:
            curr.next=l1
        else:
            curr.next=l2
        return head
                
                
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        