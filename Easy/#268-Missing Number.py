"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""
# 思路：主要应用 set() 求差集的特性

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_list = set(range(0, len(nums) + 1))
        diff = list(num_list.difference(set(nums))) # 求差集

        return diff[0]


if __name__ == "__main__":

    nums = [3, 0, 1]
    solution = Solution()
    print(solution.missingNumber(nums))