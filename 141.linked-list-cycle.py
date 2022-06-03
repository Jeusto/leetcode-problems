#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#        preview self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Slow & fast
        if not head:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False

            slow = slow.next
            fast = fast.next.next

        return True

        # Dictionary
        h = {}

        while head:
            if head in h:
                return True

            h[head] = 1
            head = head.next

        return False


# @lc code=end
