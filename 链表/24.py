# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        while p.next and p.next.next:
            temp = p.next
            temp1 = p.next.next.next
            p.next = p.next.next
            p.next.next = temp
            temp.next = temp1
            p = p.next.next
        return dummy.next
