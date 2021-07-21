/*
 * @lc app=leetcode id=125 lang=java
 *
 * [125] Valid Palindrome
 */

// @lc code=start
class Solution {

  public boolean isPalindrome(String s) {
    if (s.isEmpty()) {
      return true;
    }

    // Normalize string
    String normalized = s
      .replaceAll("[^a-zA-Z0-9]", " ")
      .replaceAll("\\s+", "")
      .toLowerCase();
    System.out.println(normalized);

    // Check if it's a palindrome
    for (int i = 0, j = normalized.length() - 1; i < j; i++, j--) {
      System.out.println(
        "i = " + i + normalized.charAt(i) + "\nj = " + j + normalized.charAt(j)
      );
      if (normalized.charAt(i) != normalized.charAt(j)) {
        return false;
      }
    }
    return true;
  }
}
// @lc code=end
