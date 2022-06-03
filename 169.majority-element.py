#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict = {}
        
        for n in nums:
            dict[n] = dict.get(n,0)+1
            if dict[n] > len(nums)//2: 
                return n
        
# @lc code=end

