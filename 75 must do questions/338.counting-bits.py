#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#


# @lc code=start
def hammingWeight(n: int) -> int:
  count = 0
  while (n):
    count += n & 1
    n = n >> 1
  return count


class Solution:

  def countBits(self, n: int) -> List[int]:
    list = []
    for i in range(n + 1):
      list.append(hammingWeight(i))
    return list


# @lc code=end
