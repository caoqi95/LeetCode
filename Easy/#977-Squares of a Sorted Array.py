# -*- coding: utf-8 -*-
"""
Given an array of integers A sorted in non-decreasing order, return an array 
of the squares of each number, also in sorted non-decreasing order.

 

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]
"""

class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        #import numpy
        #square_A = (numpy.array(A)**2)
        
        #return sorted(square_A)
        
        # faster
        return sorted(x*x for x in A)

if __name__ == "__main__":
    
    #A = [-4, -1, 0, 3, 10]
    A = [-7, -3, 2, 3, 11]
    solution = Solution()
    print(solution.sortedSquares(A))
