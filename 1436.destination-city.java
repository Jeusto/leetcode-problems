import java.util.HashMap;

/*
 * @lc app=leetcode id=1436 lang=java
 *
 * [1436] Destination City
 */

// @lc code=start
class Solution {

  HashMap<String, String> paths_map = new HashMap<>();

  public String destCity(List<List<String>> paths) {
    for (List<String> list : paths) {
      paths_map.put(list.get(0), list.get(1));
    }

    for (List<String> list : paths) {
      if (!paths_map.containsKey(list.get(1))) {
        return list.get(1);
      }
    }

    return "";
  }
}
// @lc code=end
