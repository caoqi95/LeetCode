"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # 将 list 转换成所代表的整数，进行加 1 操作
        list_to_num = int("".join([str(x) for x in digits])) + 1
        # 将加 1 后的结果转换为 list 表示
        num_to_list = [int(x) for x in str(list_to_num)]


        print(num_to_list)
        return num_to_list



if __name__ == '__main__':
    digits = [9,9]
    solution = Solution()
    solution.plusOne(digits)