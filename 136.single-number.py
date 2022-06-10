#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Xor
        res = 0
        for n in nums:
            res = res ^ n
        return res

        # Hashmap
        h = {}

        for n in nums:
            if n in h:
                h.pop(n)
            else:
                h[n] = ""

        return next(iter(h))


# @lc code=end
