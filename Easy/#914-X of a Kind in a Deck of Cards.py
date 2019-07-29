# -*- coding: utf-8 -*-
"""
In a deck of cards, each card has an integer written on it.

Return true if and only if you can choose X >= 2 such that it is possible to 
split the entire deck into 1 or more groups of cards, where:

Each group has exactly X cards.
All the cards in each group have the same integer.
 

Example 1:

Input: [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4]
Example 2:

Input: [1,1,1,2,2,2,3,3]
Output: false
Explanation: No possible partition.
Example 3:

Input: [1]
Output: false
Explanation: No possible partition.
Example 4:

Input: [1,1]
Output: true
Explanation: Possible partition [1,1]
Example 5:

Input: [1,1,2,2,2,2]
Output: true
Explanation: Possible partition [1,1],[2,2],[2,2]
"""
import collections
from functools import reduce
import math

class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        # solution 1: Brute Force
        """
        解题思路：
            将 N 张牌分为 k 堆 X 张，满足条件的话就有：N % X == 0；
            然后在每堆牌中有 i 张牌，都满足 i % X == 0。
            满足这两个条件都可以得到正确的结果。
        """
        count = collections.Counter(deck)
        N = len(deck)
        for X in range(2, N+1):
            if N % X == 0:
                if all(v % X == 0 for v in count.values()):
                    return True
        return False
        
        # solution 2: Greatest Common Divisor
        """
        
        vals = collections.Counter(deck).values()
        return reduce(math.gcd, vals) >= 2
        """

if __name__ == "__main__":
    
    #deck = [1, 2, 3, 4, 4, 3, 2, 1]
    deck = [1, 1, 2, 3, 3]
    solution = Solution()
    print(solution.hasGroupsSizeX(deck))