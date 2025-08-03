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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        int listSize = 0;
        ListNode tmp = head;
        while (tmp != null) {
            tmp = tmp.next;
            listSize++;
        }
        System.out.println(listSize);
        if (n == listSize) return head.next;
        ListNode prev = null;
        tmp = head;
        for (int i = 0; i < listSize-n; i++) {
            prev = tmp;
            tmp = tmp.next;
        }
        if (tmp == null) {
            prev.next = null;
        } else {
            prev.next = tmp.next;
        }
        return head;
    }
}