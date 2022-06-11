#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def isSymmetricRecursive(left, right):
    if left == None or right == None:
        return left == right
    if left.val != right.val:
        return False

    return isSymmetricRecursive(left.left, right.right) and isSymmetricRecursive(
        left.right, right.left
    )


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return root == None or isSymmetricRecursive(root.left, root.right)

        # Iterative
        if root is None:
            return True
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val == right.val:
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
            else:
                return False
        return True


# @lc code=end
