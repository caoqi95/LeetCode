"""
In a given integer array nums, there is always exactly one largest element.

Find whether the largest element in the array is at least twice as much as 
every other number in the array.

If it is, return the index of the largest element, otherwise return -1.

Example 1:

Input: nums = [3, 6, 1, 0]
Output: 1
Explanation: 6 is the largest integer, and for every other number in the array x,
6 is more than twice as big as x.  The index of value 6 is 1, so we return 1.
 

Example 2:

Input: nums = [1, 2, 3, 4]
Output: -1
Explanation: 4 isn't at least as big as twice the value of 3, so we return -1.
 

Note:

nums will have a length in the range [1, 50].
Every nums[i] will be an integer in the range [0, 99].
"""
class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return -1
        maxi = max(nums)
        n_nums = [i for i in nums if i < maxi]
        isTwice = [maxi >= 2*i for i in n_nums]
        true_n = [1 for i in isTwice if i == True]
        if len(true_n) == len(n_nums):
            return nums.index(maxi)

        return -1
        """
        # 简洁版
        m = max(nums)
        if all(m >= 2*x for x in nums if x != m):
            return nums.index(m)
        return -1
        """

if __name__ == "__main__":

    # nums = [3, 6, 1, 0]  # return 1
    # nums = [1, 2, 3, 4]  # return -1
    # nums = []  # return -1
    nums = [1]  # return 0
    solution = Solution()
    print(solution.dominantIndex(nums))