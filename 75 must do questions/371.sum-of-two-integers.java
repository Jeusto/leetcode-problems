/*
 * @lc app=leetcode id=371 lang=java
 *
 * [371] Sum of Two Integers
 */

// @lc code=start
class Solution {

  public int getSum(int a, int b) {
    if (a == 0) {
      return b;
    }
    if (b == 0) {
      return a;
    }
    while (b != 0) {
      int sum = a ^ b;
      int carry = (a & b);
      carry = carry << 1;

      a = sum;
      b = carry;
    }
    return a;
  }
}
// @lc code=end
