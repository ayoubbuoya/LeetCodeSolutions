#
# @lc app=leetcode id=1672 lang=python
#
# [1672] Richest Customer Wealth
#

# @lc code=start



class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        # accounts[row][col]
        # row is customer name
        # col is bank name
        max_wealth = 0
        for customer in accounts:
            cust_wealth = 0
            for bank in customer:
                cust_wealth += bank
            if cust_wealth > max_wealth:
                max_wealth = cust_wealth

        return max_wealth


# @lc code=end
