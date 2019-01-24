# coding=utf-8
"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""
import string
# import operator # 用于判断两个字符串是否相等


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # 自己的解法，虽然长，但是好理解，耗时短

        if s is None:
            return True

        # 标点符号集合
        p = string.punctuation
        # print(p)

        # 先转换为小写
        s = s.lower().strip(' ')

        list_str = []
        for i in s:
            if i not in p and i != ' ':
                list_str.append(i)
        # print(list_str)

        # 逆转 list_str
        reserve_s = list_str[::-1]
        # print(reserve_s)

        # print(operator.eq(list_str, reserve_s))
        # return operator.eq(s, reserve_s)

        print(list_str == reserve_s)
        return list_str == reserve_s

        """
        # 别人的方法：短小精悍, 但是耗时长
        
        s = s.lower()
        filtered = list(filter(lambda a: a.isalpha() or a.isdigit(), s))

        print(filtered == filtered[::-1])
        return filtered == filtered[::-1]
        """


if __name__ == '__main__':

    s = "A man, a plan, a canal: Panama"
    # s = "a car, a people"
    # s = " "
    solution = Solution()
    solution.isPalindrome(s)
