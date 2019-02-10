# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        ptr1=head
        ptr2=head
        while (ptr1 is not None):
            ptr1=ptr1.next
            if ptr1 is not None:
                ptr1=ptr1.next
            else:
                break
            ptr2=ptr2.next
            if ptr1==ptr2:
                break
        if ptr1 is None:
            return
        ptr2=head
        while(True):
            if ptr1==ptr2:
                return ptr1
            ptr1=ptr1.next
            ptr2=ptr2.next
        return                
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        
        