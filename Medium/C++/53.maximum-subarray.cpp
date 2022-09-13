/*
 * @lc app=leetcode id=53 lang=cpp
 *
 * [53] Maximum Subarray
 */
#include <iostream>
#include <vector>

using namespace std;

void printIntVector(vector<int> &nums)
{
    for (auto itr = nums.begin(); itr != nums.end(); itr++)
    {
        cout << "Vector[" << itr - nums.begin() << "] : " << *itr << endl;
    }
}
// @lc code=start
class Solution
{
public:
    int maxSubArray(vector<int> &nums)
    {
        int maxSum = nums[0];
        int sum = nums[0];
        for (int i = 1; i < nums.size(); i++)
        {
            sum = max(nums[i] + sum, nums[i]);
            if (sum > maxSum)
            {
                maxSum = sum;
            }
        }
        return maxSum;
    }
};
// @lc code=end

int main()
{
    Solution sol;
    vector<int> nums{-2, 1, -3, 4, -1, 2, 1, -5, 4};
    printIntVector(nums);
    int res = sol.maxSubArray(nums);
    cout << res << endl;
    return 0;
}