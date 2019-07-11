# -*- coding: utf-8 -*-
"""
Given an array A of non-negative integers, half of the integers in A are odd, 
and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; 
and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
"""
#from itertools import chain

class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        """ Time Limit Exceeded
        
        even = [A[i] for i in range(len(A)) if A[i] % 2 == 0]
        odd = [A[i] for i in range(len(A)) if A[i] not in even]     
        res = list(chain.from_iterable(zip(even, odd)))
        
        return res
        """
        
        # solution 
        
        N = len(A)
        ans = [None] * N
        
        t = 0
        for i, x in enumerate(A):
            if x % 2 == 0:
                ans[t] = x
                t += 2
        t = 1
        for i, x in enumerate(A):
            if x % 2 == 1:
                ans[t] = x
                t += 2
        
        # We could have also used slice asssignment
        # ans[::2] = (x for x in A if x % 2 == 0)
        # and[1::2] = (x for x in A if x % 2 == 1)
        
        return ans
        
    

if __name__ == "__main__":
    
    A = [4, 2, 5, 7]
    solution = Solution()
    print(solution.sortArrayByParityII(A))