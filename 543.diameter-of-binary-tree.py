#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # With global variable
        self.currentMax = 0

        def depth(root):
            if not root:
                return 0

            left, right = depth(root.left), depth(root.right)
            self.currentMax = max(self.currentMax, left + right)

            return 1 + max(left, right)

        depth(root)
        return self.currentMax

        # Without global variable but tuple returned every time


# @lc code=end
