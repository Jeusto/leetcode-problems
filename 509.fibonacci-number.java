/*
 * @lc app=leetcode id=509 lang=java
 *
 * [509] Fibonacci Number
 */

// @lc code=start
class Solution {

  Map<Integer, Integer> fibonacci = new HashMap();

  public int fib(int n) {
    if (n <= 0) {
      return 0;
    }
    if (n == 1) {
      return 1;
    }
    if (fibonacci.get(n) == null) {
      fibonacci.put(n, fib(n - 1) + fib(n - 2));
    }
    return fibonacci.get(n);
  }
}
// @lc code=end
