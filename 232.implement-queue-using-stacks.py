#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
class MyQueue:
    def __init__(self):
        self.pushStack = []
        self.peekAndPopStack = []

    def push(self, x: int) -> None:
        self.pushStack.append(x)

    def pop(self) -> int:
        self.stackTransfer()
        return self.peekAndPopStack.pop()

    def peek(self) -> int:
        self.stackTransfer()
        return self.peekAndPopStack[-1]

    def stackTransfer(self):
        if len(self.peekAndPopStack) == 0:
            while self.pushStack:
                self.peekAndPopStack.append(self.pushStack.pop())
        return self.peekAndPopStack[-1]

    def empty(self) -> bool:
        return len(self.pushStack) + len(self.peekAndPopStack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end
