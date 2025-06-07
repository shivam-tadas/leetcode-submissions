# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        if not head.next:
            return head
        
        currHead = head
        tmp = head
        n = 0

        while tmp:
            tmp = tmp.next
            n += 1

        print(n)
        k %= n

        while k:
            ptr = currHead
            prev = None

            while ptr.next:
                prev = ptr
                ptr = ptr.next

            prev.next = None
            ptr.next = currHead
            currHead = ptr
            k -= 1

        return currHead