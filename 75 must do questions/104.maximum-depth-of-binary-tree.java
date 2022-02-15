/*
 * @lc app=leetcode id=104 lang=java
 *
 * [104] Maximum Depth of Binary Tree
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {

  static int recursiveMaxDepth(TreeNode root) {
    if (root == null) return 0;
    return (
      Math.max(recursiveMaxDepth(root.left), recursiveMaxDepth(root.right)) + 1
    );
  }

  public int maxDepth(TreeNode root) {
    return recursiveMaxDepth(root);
  }
}
// @lc code=end
