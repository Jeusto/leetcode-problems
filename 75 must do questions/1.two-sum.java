import java.util.Map;

/*
 * @lc app=leetcode id=1 lang=java
 *
 * [1] Two Sum
 */

// @lc code=start
class Solution {

  public int[] twoSum(int[] numbers, int target) {
    Map<Integer, Integer> map = new HashMap<Integer, Integer>();

    for (int i = 0; i < numbers.length; ++i) {
      if (map.containsKey(target - numbers[i])) {
        return new int[] { map.get(target - numbers[i]), i };
      }
      map.put(numbers[i], i);
    }
    return null;
  }
}
// @lc code=end
