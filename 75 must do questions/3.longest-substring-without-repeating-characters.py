#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start


class Solution:

  def lengthOfLongestSubstring(self, s: str) -> int:
    # First solution using a string
    max = 1 if s else 0
    seen = ''

    for i in range(len(s)):
      if s[i] not in seen:
        seen = seen + s[i]
      else:
        seen = seen[seen.index(s[i]) + 1:] + s[i]
      max = max if max > len(seen) else len(seen)

    return max

    # Second solution using a set
    # max = 0
    # seen = set()
    # left = 0
    # right = 0

    # while right < len(s):
    #   while s[right] in seen:
    #     seen.remove(s[left])
    #     left += 1

    #   seen.add(s[right])
    #   right += 1
    #   max = max(max, len(seen))

    # return max


# @lc code=end
