"""
Write a function that takes an unsigned integer and return the number of '1' bits it has 
(also known as the Hamming weight).


Example 1:

Input: 00000000000000000000000000001011
Output: 3
Explanation: The input binary string 00000000000000000000000000001011 has 
a total of three '1' bits.
Example 2:

Input: 00000000000000000000000010000000
Output: 1
Explanation: The input binary string 00000000000000000000000010000000 has 
a total of one '1' bit.
Example 3:

Input: 11111111111111111111111111111101
Output: 31
Explanation: The input binary string 11111111111111111111111111111101 has 
a total of thirty one '1' bits.
"""
from collections import Counter

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = str('{:032b}'.format(n))# 转换成 32 位的字符串二进制形式
        cnt = Counter(i for i in n if i == '1')
        return cnt['1']


if __name__ == "__main__":

    n = int('00000010100101000001111010011100',2) # 二进制的十进制形式输入
    solution = Solution()
    print(solution.hammingWeight(n))