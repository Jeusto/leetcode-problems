#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        res, prev = 0, 0

        d = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        # Worse: for c in s[::-1]:
        for c in reversed(s):
            if d[c] >= prev:
                res += d[c]
            else:
                res -= d[c]
            prev = d[c]

        return res

        # Slower but cleverer
        # d = {
        #             "I": 1,
        #             "V": 5,
        #             "X": 10,
        #             "L": 50,
        #             "C": 100,
        #             "D": 500,
        #             "M": 1000,
        #         }

        # s = s.replace("IV", "IIII").replace("IX", "VIIII")
        # s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        # s = s.replace("CD", "CCCC").replace("CM", "DCCCC")

        # return sum(map(d.get, s))


# @lc code=end
