/*
 * @lc app=leetcode id=1920 lang=java
 *
 * [1920] Build Array from Permutation
 */

// @lc code=start
class Solution {

  public int[] buildArray(int[] nums) {
    int[] ans = new int[nums.length];
    for (int i : nums) {
      ans[i] = nums[nums[i]];
    }
    return ans;
  }
}
// @lc code=end
