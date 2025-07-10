# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        newList = ListNode(l1.val + l2.val)
        if l1.val + l2.val > 9:
            newList.val -= 10
            carry = 1
        ptr = newList
        nextNode = None
        l1 = l1.next
        l2 = l2.next
        while l1 != None or l2 != None: # Find sum digit by digit and forward the carry 1
            digitSum = 0
            if l1 == None:  # When list l1 is over
                if carry == 1:
                    digitSum = l2.val + carry
                    carry = 0
                else:
                    digitSum = l2.val
                if digitSum > 9:
                    carry = 1
                    digitSum -= 10
                nextNode = ListNode(digitSum)
                ptr.next = nextNode
                ptr = ptr.next
                l2 = l2.next
                continue

            if l2 == None:  # When list l2 is over
                if carry == 1:
                    digitSum = l1.val + carry
                    carry = 0
                else:
                    digitSum = l1.val
                
                if digitSum > 9:
                    carry = 1
                    digitSum -= 10
                nextNode = ListNode(digitSum)
                ptr.next = nextNode
                ptr = ptr.next
                l1 = l1.next
                continue

            if carry == 1:
                digitSum = l1.val + l2.val + carry
                carry = 0
            else:
                digitSum = l1.val + l2.val

            if digitSum > 9:
                carry = 1
                digitSum -= 10
            
            nextNode = ListNode(digitSum)
            ptr.next = nextNode
            ptr = ptr.next
            l1 = l1.next
            l2 = l2.next

        if carry == 1:
            ptr.next = ListNode(1)  # Add last carried forward digit at the end

        return newList