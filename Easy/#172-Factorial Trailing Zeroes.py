"""
Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.
"""
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 5 的附近一定存在与之相匹配的偶数，从而可以形成 0 ，所以只要判断 5 的整数倍就行
        cnt = 0
        while n >=5:
            n //= 5
            cnt += n
        return cnt
        
        # 写成递归形式
        # return n/5 + self.trailingZeroes(n/5) if n >= 5 else 0


        

if __name__ == "__main__":
    
    n = 25 # 尾随 6 个 0
    # n = 5 # 尾随 1 个 0
    # n = 3 # 没有 0 尾随
    solution = Solution()
    ans = solution.trailingZeroes(n)
    print(ans)