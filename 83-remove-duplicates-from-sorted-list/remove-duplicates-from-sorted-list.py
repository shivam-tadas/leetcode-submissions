# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
            
        ptr = head
        newHead = ListNode()
        ptr2 = newHead
        prev = None

        while ptr != None:
            if not (ptr.next and ptr.next.val == ptr.val):  # Do nothing in case of duplicate values
                ptr2.val = ptr.val  # Otherwise, add this value to new linked list
                ptr2.next = ListNode()
                prev = ptr2
                ptr2 = ptr2.next

            ptr = ptr.next

        prev.next = None

        return newHead