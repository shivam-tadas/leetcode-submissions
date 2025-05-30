# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        prev = None
        ptr = None
        nextNode = head

        while nextNode != None:
            prev = ptr
            ptr = nextNode
            nextNode = ptr.next
            ptr.next = prev

        return ptr