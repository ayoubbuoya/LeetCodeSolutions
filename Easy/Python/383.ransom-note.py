#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        letters = set(ransomNote)  # set because it removes duplicate letters
        for letter in letters:
            if ransomNote.count(letter) > magazine.count(letter):
                return False
        return True


# @lc code=end
print(Solution().canConstruct(ransomNote="baa", magazine="aab"))
