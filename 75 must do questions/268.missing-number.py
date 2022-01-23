#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#


# @lc code=start
class Solution:

  def missingNumber(self, nums: List[int]) -> int:
    # Sum approach (possibility of integer overflow for very large numbers)
    n = len(nums)
    expectedSum = n * (n + 1) / 2
    listSum = sum(nums)
    print(n)
    print(expectedSum)
    print(listSum)

    return int(expectedSum - listSum)

    # Xor approach


# @lc code=end