package medium;

import java.util.Arrays;

/*
 * @lc app=leetcode id=807 lang=java
 *
 * [807] Max Increase to Keep City Skyline
 */

// @lc code=start
class Solution {

  public int maxIncreaseKeepingSkyline(int[][] grid) {
    int rowsNumber = grid.length;
    int colsNumber = grid[0].length;
    int maximumTotalSum = 0;

    int[] maxRows = new int[rowsNumber];
    int[] maxCols = new int[colsNumber];

    for (int r = 0; r < grid.length; r++) {
      for (int c = 0; c < grid[0].length; c++) {
        maxRows[r] = Math.max(maxRows[r], grid[r][c]);
        maxCols[c] = Math.max(maxCols[c], grid[r][c]);
      }
    }

    for (int r = 0; r < grid.length; r++) {
      for (int c = 0; c < grid[0].length; c++) {
        int currentValue = grid[r][c];
        int minMax = Math.min(maxRows[r], maxCols[c]);

        if (currentValue < minMax) {
          maximumTotalSum += minMax - currentValue;
        }
      }
    }

    return maximumTotalSum;
  }
}
// @lc code=end
