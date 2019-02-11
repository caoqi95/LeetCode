"""
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: 
Starting with any positive integer, replace the number by 
the sum of the squares of its digits, and repeat the process 
until the number equals 1 (where it will stay), or it loops 
endlessly in a cycle which does not include 1. Those numbers 
for which this process ends in 1 are happy numbers.
"""
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        cycle = list() # 用于存储所有的 n 值
        while n != 1 and n not in cycle:
            cycle.append(n)
            n = sum(int(i) ** 2 for i in str(n)) # 求平方和
        
        return n == 1


if __name__ == '__main__':

    n = 19
    solution = Solution()
    print(solution.isHappy(n))
