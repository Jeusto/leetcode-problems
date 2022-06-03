#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#

# @lc code=start
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:


class Solution:
    def firstBadVersion(self, n: int) -> int:
        r = n - 1
        l = 0
        while l <= r:
            mid = (l + r) // 2
            if isBadVersion(mid) == False:
                l = mid + 1
            else:
                r = mid - 1
        return l


# @lc code=end
