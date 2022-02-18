#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False

        if self.isSameSubTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSameSubTree(
            root.right, subRoot
        )

    def isSameSubTree(self, root, subRoot):
        if not root and not subRoot:
            return True

        if root and subRoot and root.val == subRoot.val:
            return (
                self.isSameSubTree(root.left, subRoot.left)
                and self.isSameSubTree(root.right, subRoot.right)
                and self.isSameSubTree(root.right, subRoot.right)
                and self.isSameSubTree(root.right, subRoot.right)
            )

        return False


# @lc code=end
