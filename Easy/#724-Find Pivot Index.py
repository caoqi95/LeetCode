"""
Given an array of integers nums, write a method that returns the "pivot" index of this array.

We define the pivot index as the index where the sum of the numbers to the left of the index is 
equal to the sum of the numbers to the right of the index.

If no such index exists, we should return -1. If there are multiple pivot indexes, you should 
return the left-most pivot index.

Example 1:

Input: 
nums = [1, 7, 3, 6, 5, 6]
Output: 3
Explanation: 
The sum of the numbers to the left of index 3 (nums[3] = 6) is equal to the sum of numbers to 
the right of index 3.
Also, 3 is the first index where this occurs.
 

Example 2:

Input: 
nums = [1, 2, 3]
Output: -1
Explanation: 
There is no index that satisfies the conditions in the problem statement.
"""
class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 计算数组的总和 S
        # 累加左边的和 leftsum
        # 剩余右边的和就等于 S - leftsum - n
        # 循环判断 leftsum == S - leftsum - n 即可
        
        S = sum(nums)
        leftsum = 0
        for i, n in enumerate(nums):
            if leftsum == S - leftsum - n:
                return i
            leftsum += n
        return -1

        
if __name__ == "__main__":

    # nums = [1, 7, 3, 6, 5, 6]
    # nums = [6, 5, 1, 7, 4]
    nums = [1, 2, 3]
    solution = Solution()
    print(solution.pivotIndex(nums))