#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    # Using simple array
    def climbStairs(self, n: int) -> int:
        t = [0, 1, 2]
        for i in range(3, n + 1):
            t.append(t[i - 1] + t[i - 2])

        return t[n]

    # Using hashmap/dict
    # h = {0: 0, 2: 2, 1: 1}

    # def climbStairs(self, n: int) -> int:
    #     if n in self.h:
    #         return self.h[n]

    #     current = self.climbStairs(n - 1) + self.climbStairs(n - 2)
    #     self.h[n] = current

    #     return current


# @lc code=end
