#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
from typing import List
# @lc code=start


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            j = 1
            while j + i < len(nums):
                if nums[i] + nums[i+j] == target:
                    return [i, i + j]
                else:
                    j += 1
        return []


# @lc code=end
print(Solution().twoSum([3, 2, 3], 6))
