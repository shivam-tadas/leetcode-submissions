# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lA, lB = 0, 0   # Lengths of lists A and B
        ptrA, ptrB = headA, headB   # Pointers to lists

        while ptrA != None: # Find length of A
            lA += 1
            ptrA = ptrA.next

        while ptrB != None: # Find length of B
            lB += 1
            ptrB = ptrB.next

        ptrA, ptrB = headA, headB   # Reset pointers
        if lA > lB:
            for i in range(lA - lB):
                ptrA = ptrA.next

        if lB > lA:
            for i in range(lB - lA):
                ptrB = ptrB.next    # Move the pointer to longer list just forward enough such that equal number of nodes are present ahead of both pointers
        
        while ptrA != ptrB and ptrA != None and ptrB != None:
            ptrA = ptrA.next
            ptrB = ptrB.next    # Try to find an intersection by traversing

        if ptrA == ptrB:
            return ptrA

        return None # If no intersection is found