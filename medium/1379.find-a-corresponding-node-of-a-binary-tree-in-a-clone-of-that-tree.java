package medium;

/*
 * @lc app=leetcode id=1379 lang=java
 *
 * [1379] Find a Corresponding Node of a Binary Tree in a Clone of That Tree
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Solution {

  public final TreeNode getTargetCopy(
    final TreeNode original,
    final TreeNode cloned,
    final TreeNode target
  ) {
    if (original == null || target == null) {
      return null;
    } else if (original == target) {
      return cloned;
    } else {
      TreeNode left = getTargetCopy(original.left, cloned.left, target);
      if (left != null) {
        return left;
      }
      TreeNode right = getTargetCopy(original.right, cloned.right, target);
      if (right != null) {
        return right;
      }

      return null;
    }
  }
}
// @lc code=end
