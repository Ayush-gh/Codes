# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1=head.next
        p2=head
        while p1!=None:
            p2.val=p2.val+p1.val
            if p1.val ==0 and p1.next!=None:
                p2.next=p1
                p2=p1
            p1=p1.next
        p2.next=None
        return head
