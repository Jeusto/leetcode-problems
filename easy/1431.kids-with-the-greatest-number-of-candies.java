/*
 * @lc app=leetcode id=1431 lang=java
 *
 * [1431] Kids With the Greatest Number of Candies
 */

// @lc code=start
class Solution {

  public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
    List<Boolean> result = new ArrayList<Boolean>();

    int maxVal = 0;
    for (int i : candies) {
      maxVal = i > maxVal ? i : maxVal;
    }

    for (int i = 0; i < candies.length; i++) {
      result.add(candies[i] + extraCandies >= maxVal ? true : false);
    }
    return result;
  }
}
// @lc code=end
