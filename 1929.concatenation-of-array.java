/*
 * @lc app=leetcode id=226 lang=java
 *
 * [226] Invert Binary Tree
 */

// @lc code=start
class Solution {

  public int[] getConcatenation(int[] nums) {
    int n = nums.length;
    int[] ans = new int[n * 2];
    for (int i = 0; i < n * 2; ++i) {
      ans[i] = nums[i % n];
    }
    return ans;
  }
}
// @lc code=end
