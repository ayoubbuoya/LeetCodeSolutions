/*
 * @lc app=leetcode id=217 lang=cpp
 *
 * [217] Contains Duplicate
 */
#include <iostream>
#include <vector>
#include <algorithm>

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
    bool containsDuplicate(vector<int> &nums)
    {
        // sort vector
        sort(nums.begin(), nums.end());
        for (int i = 0; i < nums.size() - 1; i++)
        {
            if (nums[i] == nums[i + 1])
            {
                return true;
            }
        }
        return false;
    }
};
// @lc code=end

int main()
{
    Solution sol;
    vector<int> nums{1, 2, 3, 4};
    bool res = sol.containsDuplicate(nums);
    cout << res << endl;
    return 0;
}