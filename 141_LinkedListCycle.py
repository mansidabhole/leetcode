# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if not head:
            return False
        ptr1=head
        ptr2=ptr1.next
        while (ptr2!= None and ptr2!=ptr1):
            ptr1=ptr1.next
            ptr2=ptr2.next
            if ptr2 is None:
                break
            ptr2=ptr2.next
        if ptr2 is not None:
            return True
        else:
            return False
        """
        :type head: ListNode
        :rtype: bool
        """
        