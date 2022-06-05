#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Calculating height and balance together
        def dfsHeight(root):
            if not root:
                return 0

            leftHeight = dfsHeight(root.left)
            if leftHeight == -1:
                return -1

            rightHeight = dfsHeight(root.right)
            if rightHeight == -1:
                return -1

            if abs(leftHeight - rightHeight) > 1:
                return -1

            return max(leftHeight, rightHeight) + 1

        return dfsHeight(root) != -1

        # Calculating height and balance separately
        def height(root):
            if not root:
                return -1
            return max((height(root.left) + 1), (height(root.right) + 1))

        if not root:
            return True

        return (
            abs(height(root.left) - height(root.right)) <= 1
            and self.isBalanced(root.left)
            and self.isBalanced(root.right)
        )


# @lc code=end
