# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newList = ListNode()
        ptr = newList
        while list1 and list2:
            if list1.val == list2.val:
                ptr.next = ListNode(list1.val)
                ptr.next.next = ListNode(list2.val)
                ptr = ptr.next.next
                list1 = list1.next
                list2 = list2.next
            elif list1.val < list2.val:
                ptr.next = ListNode(list1.val)
                ptr = ptr.next
                list1 = list1.next
            else:
                ptr.next = ListNode(list2.val)
                ptr = ptr.next
                list2 = list2.next

        while list1:
            ptr.next = ListNode(list1.val)
            ptr = ptr.next
            list1 = list1.next

        while list2:
            ptr.next = ListNode(list2.val)
            ptr = ptr.next
            list2 = list2.next

        return newList.next