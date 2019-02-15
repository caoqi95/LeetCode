"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        """ 好理解，速度慢 
        d = []
        for i in nums:
            if d == [] or i not in d:
                d.append(i)
            else:
                d.remove(i)
            
        return not (len(d) == len(nums))
        """
        # 速度快
        return not (len(set(nums)) == len(nums))

if __name__ == "__main__":

    # nums = [0]
    nums = [1, 2, 3, 4]
    solution = Solution()
    print(solution.containsDuplicate(nums))