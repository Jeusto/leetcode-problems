#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = {}

        for c in ransomNote:
            if c in dic:
                dic[c] += 1
            else:
                dic[c] = 1

        for c in magazine:
            if c in dic:
                if dic[c] == 1:
                    dic.pop(c)
                else:
                    dic[c] -= 1

        return len(dic.keys()) == 0

        # for i in set(ransomNote):
        #     if magazine.count(i) < ransomNote.count(i):
        #         return False
        # return True


# @lc code=end
