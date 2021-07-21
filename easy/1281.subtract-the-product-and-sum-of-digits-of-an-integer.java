/*
 * @lc app=leetcode id=1281 lang=java
 *
 * [1281] Subtract the Product and Sum of Digits of an Integer
 */

// @lc code=start
class Solution {

  public int subtractProductAndSum(int n) {
    String number = Integer.toString(n);
    int product = Character.getNumericValue(number.charAt(0));
    int sum = Character.getNumericValue(number.charAt(0));

    for (int i = 1; i < number.length(); i++) {
      product *= Character.getNumericValue(number.charAt(i));
      sum += Character.getNumericValue(number.charAt(i));
    }

    return product - sum;
  }
}
// @lc code=end
