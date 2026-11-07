/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node next;

    public Node() {}
    
    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, Node _left, Node _right, Node _next) {
        val = _val;
        left = _left;
        right = _right;
        next = _next;
    }
};
*/

class Solution {
    List<Node> BFS;
    public Node connect(Node root) {
        if (root == null) return null;

        BFS = new ArrayList<>();
        traverseBFS(root);
        // for (Node curr : BFS) {
        //     System.out.print(curr.val + " ");
        // }
        // System.out.println();
        connectHelper();
        return root;
    }

    private void traverseBFS(Node root) {
        Deque<Node> queue = new ArrayDeque<>();
        queue.addLast(root);
        while (!queue.isEmpty()) {
            Node curr = queue.pollFirst();
            if (curr.left != null) queue.addLast(curr.left);
            if (curr.right != null) queue.addLast(curr.right);
            BFS.add(curr);
        }
    }

    private void connectHelper() {
        int i;
        Node curr = BFS.get(0), prev = BFS.get(0);
        for (i = 1; i < BFS.size(); ++i) {
            prev = BFS.get(i-1);
            curr = BFS.get(i);
            if (i+1 > 0 && (i+1 & i) == 0)
                prev.next = null;
            else
                prev.next = curr;
        }
        curr.next = null;
    }
}