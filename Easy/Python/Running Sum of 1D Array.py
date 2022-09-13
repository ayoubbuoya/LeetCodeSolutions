class Solution:
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sum_list = []
        res = 0
        for i in range(len(nums)):
            res += nums[i]
            sum_list.append(res)
        return sum_list


nums = [1, 2, 3, 4]
print(Solution().runningSum(nums))
