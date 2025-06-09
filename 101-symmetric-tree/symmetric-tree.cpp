/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isMirror(TreeNode* n1, TreeNode* n2) {
        if (n1 == NULL && n2 == NULL) return true;
        if (n1 == NULL || n2 == NULL) return false; // In case either node is empty
        
        return n1->val == n2->val && isMirror(n1->left, n2->right) && isMirror(n1->right, n2->left);
    }

    bool isSymmetric(TreeNode* root) {
        if (root == NULL) return false; // Empty tree

        return isMirror(root->left, root->right);   // Check for symmetry
    }
};