/*
 * @lc app=leetcode id=1529 lang=java
 *
 * [1529] Bulb Switcher IV
 */

// @lc code=start
class Solution {
    public int minFlips(String target) {
        // One liner
        return (target.split("10", -1).length - 1) * 2 + (target.charAt(target.length()-1) == '1' ? 1 : 0);
    }
}
// @lc code=end

