# -*- coding: utf-8 -*-
"""
Given an array A of integers, return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]
 

Example 1:

Input: [2,1]
Output: false
Example 2:

Input: [3,5,5]
Output: false
Example 3:

Input: [0,3,2,1]
Output: true
 

Note:

0 <= A.length <= 10000
0 <= A[i] <= 10000 
"""

class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        # solution :
        """
        首先逐渐递增 index i, 如果数组单调递增且 i 没超出范围，执行 i += 1；
        然后需要注意的是顶峰不出现在最开始和最末尾，一旦出现则不是 Valid mountain array；
        最后逐渐递增 index i, 如果数组单调递减且 i 没超出范围，执行 i += 1；
        最后判断 i 是否等于 len(A) - 1，是的话，该数组是 Valid mountain array。
        """
        N = len(A)
        i = 0 
        
        # walk up
        while i+1 < N and A[i] < A[i+1]:
            i += 1
        
        # peak can't be first or last
        if i == 0 or i == N - 1:
            return False
        
        # walk down
        while i+1 < N and A[i] > A[i+1]:
            i += 1
        
        return i == N - 1
        
if __name__ == "__main__":
    
    A = [0, 3, 2, 1] # True
    #A = [2, 1] # False
    #A = [3, 5, 5] # False
    #A = [3,7,6,4,3,0,1,0] # False
    solution = Solution()
    print(solution.validMountainArray(A))