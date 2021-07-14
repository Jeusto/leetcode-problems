/*
 * @lc app=leetcode id=1769 lang=java
 *
 * [1769] Minimum Number of Operations to Move All Balls to Each Box
 */

// @lc code=start
class Solution {

  public int[] minOperations(String boxes) {
    int length = boxes.length();
    int[] answer = new int[length];
    for (int i = 0; i < length; i++) {
      for (int j = 0; j < length; j++) {
        if (boxes.charAt(j) == '1') {
          answer[i] += Math.abs(j - i);
        }
      }
    }
    return answer;
  }
}
// @lc code=end
