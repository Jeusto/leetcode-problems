/*
 * @lc app=leetcode id=419 lang=java
 *
 * [419] Battleships in a Board
 */

// @lc code=start
class Solution {
    private int count = 0;

    public int countBattleships(char[][] board) {
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[0].length; j++) {
                if (board[i][j] == 'X') {
                    // Top left cell case
                    if (i == 0 && j == 0) {
                        count++;
                    // Top row case 
                    } else if (i == 0) {
                        if (board[i][j - 1] != 'X') {
                            count++;
                        }
                    }
                    // Left column case
                    else if (j == 0) {
                        if (board[i - 1][j] != 'X') {
                            count++;
                        }
                    }
                    // Any other case
                    else if (board[i - 1][j] != 'X' && board[i][j - 1] != 'X') {
                        count++;
                    }    
                }
                
            }
        }
        return count;
    }
}
// @lc code=end

