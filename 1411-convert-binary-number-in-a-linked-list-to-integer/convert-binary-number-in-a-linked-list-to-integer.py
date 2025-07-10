# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        ptr = head
        val = 0
        while ptr:
            val *= 2
            val += ptr.val
            ptr = ptr.next

        return val