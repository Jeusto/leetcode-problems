#
# @lc app=leetcode id=235 lang=python3
#
# [235] Lowest Common Ancestor of a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        curr = root.val

        if p.val > curr and q.val > curr:
            return self.lowestCommonAncestor(root.right, p, q)

        elif p.val < curr and q.val < curr:
            return self.lowestCommonAncestor(root.left, p, q)

        else:
            return root


# @lc code=end
