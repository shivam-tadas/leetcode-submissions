# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1_ptr = list1
        l2_ptr = list2
        new_list = ListNode()
        ptr = new_list

        while l1_ptr and l2_ptr:
            if l1_ptr.val > l2_ptr.val:
                ptr.next = ListNode(l2_ptr.val)
                ptr = ptr.next
                l2_ptr = l2_ptr.next

            elif l2_ptr.val > l1_ptr.val:
                ptr.next = ListNode(l1_ptr.val)
                ptr = ptr.next
                l1_ptr = l1_ptr.next

            elif l1_ptr.val == l2_ptr.val:
                ptr.next = ListNode(l1_ptr.val)
                ptr = ptr.next
                l1_ptr = l1_ptr.next
                ptr.next = ListNode(l2_ptr.val)
                ptr = ptr.next
                l2_ptr = l2_ptr.next
        
        while l1_ptr:
            ptr.next = ListNode(l1_ptr.val)
            l1_ptr = l1_ptr.next
            ptr = ptr.next

        while l2_ptr:
            ptr.next = ListNode(l2_ptr.val)
            l2_ptr = l2_ptr.next
            ptr = ptr.next

        return new_list.next