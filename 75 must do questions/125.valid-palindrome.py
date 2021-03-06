#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s: return True
        left, right = 0, len(s)-1
        
        while left < right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left].lower() != s[right].lower():
                    return False
                left +=1; right -= 1

            else:
                if not s[left].isalnum():
                    left+=1
                if not s[right].isalnum():
                    right-=1

        return True

        
# @lc code=end

