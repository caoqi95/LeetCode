"""
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?
"""
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        """ 方法一：弹出插入法
        while(k > 0):
            last = nums.pop()
            nums.insert(0, last)
            k -= 1

        return nums
        """

        # 方法二：
        if k > len(nums):
            k = k - len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        return nums


if __name__ == "__main__":

    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 8
    solution = Solution()
    print(solution.rotate(nums, k))