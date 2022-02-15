/*
 * @lc app=leetcode id=100 lang=c
 *
 * [100] Same Tree
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool isSameSubTree(struct TreeNode* p, struct TreeNode* q) {
  if (!p && !q) {
    return true;
  }
  if ((!p && q) || (p && !q)) {
    return false;
  }
  if (p->val != q->val) {
    return false;
  }
  return (isSameSubTree(p->left, q->left) && isSameSubTree(p->right, q->right));
}

bool isSameTree(struct TreeNode* p, struct TreeNode* q) {
  return isSameSubTree(p, q);
}
// @lc code=end
