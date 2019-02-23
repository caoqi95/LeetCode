"""
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, 
then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
"""


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        sorted_nums = sorted(nums)
        is_same = [a == b for a, b in zip(nums, sorted_nums)]
        if all(is_same):
            return 0  
        else:
            index_start = is_same.index(False)
            index_end = is_same[::-1].index(False)
            shortest = len(nums) - index_end - index_start
            return  shortest
        """
        """
        # 简洁的解法一
        is_same = [a == b for a, b in zip(nums, sorted(nums))]
        return 0 if all(is_same) else len(nums) - is_same.index(Faelse) - is_same[::-1].index(False)
        """
        # 简洁的解法二
        res = [i for (i, (a, b)) in enumerate(zip(nums, sorted(nums))) if a != b]
        return 0 if not res else res[-1]-res[0]+1 if not res else res[-1]-res[0]+1

if __name__ == "__main__":

    # nums = [2, 6, 4, 8, 10, 9, 15]  # return 5
    # nums = [1, 2, 3, 4]   # return 0
    nums = [1, 3, 2, 2, 2]  # return 4
    solution = Solution()
    print(solution.findUnsortedSubarray(nums))