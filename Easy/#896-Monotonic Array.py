# -*- coding: utf-8 -*-
"""
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A 
is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.

 

Example 1:

Input: [1,2,2,3]
Output: true
Example 2:

Input: [6,5,4,4]
Output: true
Example 3:

Input: [1,3,2]
Output: false
Example 4:

Input: [1,2,4,5]
Output: true
Example 5:

Input: [1,1,1]
Output: true
"""

class Solution:
    def isMonotonic(self, A):
        
        def isIncreasing(A):
            
            count = 0
            for i in range(len(A) - 1):
                if A[i] <= A[i+1]: #or A[i] >= A[i+1]:
                    count += 1
        
            if count + 1 == len(A):
                return True
        
            return False
        
        def isDecreasing(A):
            
            count = 0
            for i in range(len(A) - 1):
                if A[i] >= A[i+1]: #or A[i] >= A[i+1]:
                    count += 1
        
            if count + 1 == len(A):
                return True
        
            return False
    
        return isIncreasing(A) or isDecreasing(A)


if __name__ == "__main__":
    
    # A = [1, 2, 2, 3]
    # A = [1, 3, 2]
    # A = [6, 5, 4, 4]
    A = [1, 2, 4, 5]
    solution = Solution()
    print(solution.isMonotonic(A))
