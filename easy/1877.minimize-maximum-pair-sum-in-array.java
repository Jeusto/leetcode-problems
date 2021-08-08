package easy;
/*
 * @lc app=leetcode id=1877 lang=java
 *
 * [1877] Minimize Maximum Pair Sum in Array
 */

// @lc code=start
class Solution {

  private int max = 0;

  public int minPairSum(int[] nums) {
    Arrays.sort(nums);
    int n = nums.length;

    for (int i = 0; i < n / 2; i++) {
      max = Math.max(max, nums[i] + nums[n - i - 1]);
    }
    return max;
  }
}
// @lc code=end
