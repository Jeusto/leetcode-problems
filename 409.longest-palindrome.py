#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> int:
        # With array
        if not s or len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        count = 256 * [0]
        for i in range(0, len(s)):
            count[ord(s[i])] += 1

        odd = 0
        for c in count:
            if c % 2 != 0:
                odd += 1

        return len(s) if odd == 0 else len(s) - odd + 1

        # With set
        # lettersSet = set()

        # for c in s:
        #     if c not in lettersSet:
        #         lettersSet.add(c)
        #     else:
        #         lettersSet.remove(c)

        # odd = len(lettersSet)

        # return len(s) if odd == 0 else len(s) - odd + 1


# @lc code=end
