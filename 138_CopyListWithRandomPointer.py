# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return
        curr=head
        while(curr.next is not None):      #inserting clone nodes
            insert=RandomListNode(curr.label)
            insert.next=curr.next
            curr.next=insert
            curr=insert.next
        insert=RandomListNode(curr.label)
        curr.next=insert
        insert.next=None
        curr=head
        copy_head=curr.next
        while(curr.next.next is not None):     #cloning the random pointers
            if curr.random is not None:
                curr.next.random=curr.random.next
            curr=curr.next.next
        if (curr.random is not None):
            if curr.random.next is not None:
                curr.next.random=curr.random.next
        curr=head
        while(curr.next.next is not None):
            copy=curr.next
            curr.next=copy.next
            copy.next=curr.next.next
            curr=curr.next
        copy=curr.next
        curr.next=None
        copy.next=None
        return copy_head
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        
        