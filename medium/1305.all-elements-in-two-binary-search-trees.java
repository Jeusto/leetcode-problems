/*
 * @lc app=leetcode id=1305 lang=java
 *
 * [1305] All Elements in Two Binary Search Trees
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
    public List<Integer> getAllElements(TreeNode root1, TreeNode root2) {
        List<Integer> list = new ArrayList<Integer>();
        
        inorder(root1,list);
        inorder(root2,list);

        Collections.sort(list);
        
        return list;
    }
    
    public void inorder(TreeNode root, List<Integer> list){
        if (root == null) {
            return;
        }
        
        list.add(root.val);
        
        inorder(root.left,list);
        inorder(root.right,list);
    }
}
// @lc code=end

