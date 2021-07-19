/*
 * @lc app=leetcode id=1720 lang=java
 *
 * [1720] Decode XORed Array
 */

// @lc code=start
class Solution {

  public int[] decode(int[] encoded, int first) {
    int[] arr = new int[encoded.length + 1];

    arr[0] = first;

    for (int i = 1; i < arr.length; i++) {
      arr[i] = 0;
    }
    System.out.println(1 ^ 2);
    return arr;
  }
}
// @lc code=end
