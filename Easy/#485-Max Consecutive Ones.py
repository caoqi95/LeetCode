"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
Note:

The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current = nums[0]
        count = {current: 0}
        cons = []
        for i in range(len(nums)):
            if nums[i] == current:
                count[current]+= 1
            else:
                current = nums[i]
                count[current] = 1
            if current == 1:
                cons.append(count[current])

        return max(cons) if cons != [] else 0


if __name__ == "__main__":

    # nums = [0, 0]
    # nums = [0, 1]
    # nums = [1, 0, 1, 1, 0, 1]
    nums = [1, 1, 0, 1, 1, 1]
    solution = Solution()
    print(solution.findMaxConsecutiveOnes(nums))