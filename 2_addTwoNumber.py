# Definition for singly-linked list.
#class ListNode(object):
 #   def __init__(self, x):
  #      self.val = x
   #     self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        current=ListNode(0)
        start=current
        carry=0
        while(True):
            if l1!=None and l2!=None:
                n1=l1.val
                n2=l2.val
                l1=l1.next
                l2=l2.next
            elif (not l1 and not l2):
                if(current.val==0):
                    p.next=None
                else:
                    p.next=current
                break
            elif not l1:
                n1=0
                n2=l2.val
                l2=l2.next
            else :
                n1=l1.val
                n2=0
                l1=l1.next
            current.val=int((current.val+(n1+n2))%10)
            carry=int(math.floor((carry+n1+n2)/10))
            p=current
            current.next=ListNode(0)
            current=current.next
            current.val=carry
        return star