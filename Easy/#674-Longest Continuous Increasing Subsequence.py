"""
Given an unsorted array of integers, find the length of longest continuous increasing subsequence (subarray).

Example 1:
Input: [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5], its length is 3. 
Even though [1,3,5,7] is also an increasing subsequence, it's not a continuous one where 5 and 7 are separated by 4. 
Example 2:
Input: [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2], its length is 1. 

Note: Length of the array will not exceed 10,000.
"""
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 滑动窗口解法:
        # 每个递增数组的边界都发生在 nums[i-1] >= nums[i] 的时候
        # 当前窗口为：nums[anchor]...nums[anchor+1]...nums[i]
        # 所以，当前窗口的长度为: i - anchor + 1
        # 循环找出最大的长度
        
        ans = anchor = 0
        for i in range(len(nums)):
            if i and nums[i-1] >= nums[i]: 
                anchor = i
            ans = max(ans, i - anchor + 1)

        return ans

if __name__ == "__main__":

    # nums = [1, 3, 5, 4, 7]  # return 3
    nums = [2, 2, 2, 2, 2]  # return 1
    # nums = [1, 3, 5, 7]  # return 4
    # nums = [1]  # return 1
    # nums = [1, 3, 5, 4, 2, 3, 4, 5] # return 4
    solution = Solution()
    print(solution.findLengthOfLCIS(nums))