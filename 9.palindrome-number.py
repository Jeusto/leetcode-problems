#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 0 and x % 10 == 0):
            return

        # Create number in reverse order
        original = x
        reversed = 0

        while x > 0:
            reversed = reversed * 10 + x % 10
            x = x // 10

        return original == reversed

        # Convert half of the integer
        # result = 0
        # while x > result:
        #     result = result * 10 + x % 10
        #     x = x // 10
        # return x == result or x == result // 10

        # Convert to string = uses extra space
        # return str(x) == str(x)[::-1]


# @lc code=end
