# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pA = headA
        pB = headB
        
        a_len = b_len = 0
        while pA:
            a_len += 1
            pA = pA.next
        
        while pB:
            b_len += 1
            pB = pB.next
        
        diff = abs(a_len - b_len)
        pA, pB = headA, headB
        if a_len > b_len:
            while diff > 0:
                pA = pA.next
                diff -= 1
        else:
            while diff > 0:
                pB = pB.next
                diff -= 1
        
        while pA and pB:
            if pA == pB:
                return pA
            pA = pA.next
            pB = pB.next
        return None



        
        