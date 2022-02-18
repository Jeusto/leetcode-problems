#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        
        parentheses = {'(':')', '{':'}','[':']'}
        stack = []

        for char in s:
            if char in parentheses:
                stack.append(char)
            elif len(stack) == 0 or parentheses[stack.pop()] != char:
                return False
        
        return len(stack) == 0

        
        
# @lc code=end

