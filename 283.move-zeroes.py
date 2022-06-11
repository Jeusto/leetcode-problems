#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # One loop
        insertPosition = -1

        for i in range(0, len(nums)):
            if nums[i] != 0:
                insertPosition += 1
                nums[insertPosition] = nums[i]
                if i != insertPosition:
                    nums[i] = 0
            


# @lc code=end
