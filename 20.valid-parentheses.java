/*
 * @lc app=leetcode id=20 lang=java
 *
 * [20] Valid Parentheses
 */

// @lc code=start
class Solution {

  public boolean isValid(String s) {
    if (s.length() % 2 != 0) {
      return false;
    }

    Stack<Character> stack = new Stack<Character>();

    for (char c : s.toCharArray()) {
      if (c == ')' || c == ']' || c == '}') {
        char top = stack.empty() ? ' ' : stack.pop();
        if (
          c == ')' &&
          top != '(' ||
          c == ']' &&
          top != '[' ||
          c == '}' &&
          top != '{'
        ) {
          return false;
        }
      } else {
        stack.push(c);
      }
    }
    return stack.isEmpty();
  }
}
// @lc code=end
