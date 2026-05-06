# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length = 0
        dummy = ListNode(0, head)
        p = head
        # while p:
        #     length += 1
        #     p = p.next
        
        # p = dummy
        # for _ in range(length - n):
        #     p = p.next
        # p.next = p.next.next
        # return dummy.next

        fast = slow = dummy
        for _ in range(n + 1):
            if fast:
                fast = fast.next
        while fast and slow:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
        

        



