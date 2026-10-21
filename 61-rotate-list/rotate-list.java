/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode rotateRight(ListNode head, int k) {
        if (head == null) return null;

        if (head.next == null) return head;

        int listLen = 0, rotationPt = 0, i;
        ListNode ptr = head, ans = null, ptr2 = null;
        while (ptr != null) {
            ptr = ptr.next;
            ++listLen;
        }
        ptr = head;
        k %= listLen;
        if (k == 0) return head;
        
        for (i = 0; i < listLen - k; ++i) ptr = ptr.next;
        ans = new ListNode(ptr.val);
        ptr = ptr.next;
        ptr2 = ans;
        for (i = 1; i < k; ++i) {
            ptr2.next = new ListNode(ptr.val);
            ptr = ptr.next;
            ptr2 = ptr2.next;
        }
        ptr = head;
        for (i = 0; i < listLen - k; ++i) {
            ptr2.next = new ListNode(ptr.val);
            ptr = ptr.next;
            ptr2 = ptr2.next;
        }
        return ans;
    }
}