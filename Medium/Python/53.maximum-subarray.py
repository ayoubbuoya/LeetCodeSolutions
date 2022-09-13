#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#
from typing import List

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums = []
        sums.append(nums[0])
        max_sum = sums[0]
        for i in range(1, len(nums)):
            sub_sum = max(sums[i - 1] + nums[i], nums[i])
            sums.append(sub_sum)
            if sums[i] > max_sum:
                max_sum = sums[i]
        return max_sum
# @lc code=end
print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
