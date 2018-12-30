"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
"""


class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        words = s.split()
        if len(words) == 0:
            l = 0
        else:
            last_word = words[-1]
            l = len(last_word)
        print(l)
        return l


if __name__ == '__main__':
    s = 'qq '
    solution = Solution()
    solution.lengthOfLastWord(s)