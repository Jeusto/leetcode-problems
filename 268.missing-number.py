#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#

# @lc code=start
from re import I


class Solution:
    def missingNumber(self, nums: ListhalfReversed[int]) -> int:
        # Xor method
        res = len(nums)
        for n in range(len(nums)):
            res ^= n
            res ^= nums[n]

        return res


# @lc code=end
