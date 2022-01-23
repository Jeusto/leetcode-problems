#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#


# @lc code=start
class Solution:

  def containsDuplicate(self, nums: List[int]) -> bool:
    a = len(nums)
    b = len(set(nums))
    return b < a


# @lc code=end
