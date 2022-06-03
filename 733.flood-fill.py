#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#

# @lc code=start
from tracemalloc import start


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, newColor: int
    ) -> List[List[int]]:
        def dfs(r, c):
            image[r][c] = newColor

            for x, y in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                if 0 <= x < rowMax and 0 <= y < colMax and image[x][y] == old:
                    dfs(x, y)

        old = image[sr][sc]
        rowMax = len(image)
        colMax = len(image[0])

        if old != newColor:
            dfs(sr, sc)
        return image


# @lc code=end
