"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return None

        # 计算每个值的个数
        stack = {}
        for i in nums:
            if i in stack:
                stack[i] += 1
            else:
                stack[i] = 1
        #print(stack)
        # 如果值的个数大于 list 长度的一半，则返回这个值
        for k, v in stack.items():
            if v > (len(nums) / 2):
                #print(k)
                return k


if __name__ == "__main__":

    # nums = [3, 2, 3]
    nums = [2,2,1,1,1,2,2]
    solution = Solution()
    solution.majorityElement(nums)