package easy;
/*
 * @lc app=leetcode id=389 lang=java
 *
 * [389] Find the Difference
 */

// @lc code=start
class Solution {

  public char findTheDifference(String s, String t) {
    int sCount = 0;
    int tCount = 0;
    for (int i = 0; i < s.length(); i++) {
      sCount += s.charAt(i);
      tCount += t.charAt(i);
    }
    tCount += t.charAt(t.length() - 1);
    return (char) (tCount - sCount);
  }
}
// @lc code=end
