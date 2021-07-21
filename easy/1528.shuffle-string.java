/*
 * @lc app=leetcode id=1528 lang=java
 *
 * [1528] Shuffle String
 */

// @lc code=start
class Solution {

  public String restoreString(String s, int[] indices) {
    char[] result = s.toCharArray();

    for (int i = 0; i < s.length(); i++) {
      result[indices[i]] = s.charAt(i);
    }

    return new String(result);
  }
}
// @lc code=end
