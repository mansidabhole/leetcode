# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        if not head:
            return
        #search for tail
        curr=head
        count=0
        while(curr.next is not None):
            prev=curr
            curr=curr.next
            count+=1
        if count%2==0:
            tail=curr
            stop=curr
        else:
            tail=prev
            stop=prev
            attach=curr
        prev=head
        curr=prev.next
        while(curr is not stop and prev is not stop):
            prev.next=curr.next
            tail.next=curr
            tail=curr
            tail.next=None
            prev=prev.next
            curr=prev.next
        if count%2==1:
            tail.next=attach
        return head
        """
        :type head: ListNode
        :rtype: ListNode
        """
        