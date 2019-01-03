"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""


class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 可以发现如下规律：
        # 1:1
        # 2:2
        # 3:3=1+2
        # 4:5=2+3
        # 5:8=3+5
        # 6:13=5+8
        # 正好是斐波那契 Fibonacci 数列
        # 在数学上，费波那契数列是以递归的方法来定义：
        # F0=0,F1=1, Fn = Fn-1 + Fn-2

        if n < 3:
            return n
        else:
            i = 3
            l = list(range(n + 1))
            print(l)
            while i <= n:
                l[i] = l[i - 1] + l[i - 2]
                i = i + 1
            print(l[n])
            return l[n]


if __name__ == '__main__':
    n = 5
    solution = Solution()
    solution.climbStairs(n)