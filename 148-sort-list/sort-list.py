# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        listNums = []
        while head is not None:
            listNums.append(head.val)   # Store all numbers in a list
            head = head.next

        print(listNums)
        listNums.sort() # Sort the list
        
        newHead = ListNode(listNums[0])
        ptr = newHead
        for i in range(1, len(listNums)):
            ptr.next = ListNode(listNums[i])    # Make a new linked list from sorted list
            ptr = ptr.next

        return newHead