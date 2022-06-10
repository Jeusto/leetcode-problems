#
# @lc app=leetcode id=844 lang=python3
#
# [844] Backspace String Compare
#

# @lc code=start
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1
        backS = backT = 0

        while i >= 0 or j >= 0:
            while i >= 0:
                if s[i] == "#":
                    i -= 1
                    backS += 1
                elif backS > 0:
                    i -= 1
                    backS -= 1
                else:
                    break

            while j >= 0:
                if t[j] == "#":
                    j -= 1
                    backT += 1
                elif backT > 0:
                    j -= 1
                    backT -= 1
                else:
                    break

            if i < 0 and j < 0:
                return True

            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False

            i -= 1
            j -= 1

        return True


# @lc code=end
