"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"
"""
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
       # one line
       #  return "" if n == 0 else self.convertToTitle((n - 1) / 26) + chr((n - 1) % 26 + ord('A'))

        res = ""
        d = ord("A")  # 返回大写 A 对应的 ASSCII 码-65

        while n > 0: # 当 n 满足条件的时候，一直循环
            y = (n - 1) % 26   # 取模 - 返回出发的余数
            n = (n - 1) // 26  # 返回商的整数部分
            s = chr(y + d) # 生成对应的大写字符
            res = "".join((s, res)) # 返回循环中得到的所有结果
        print(res)
        return res

if __name__ == "__main__":

    n = 701
    solution = Solution()
    solution.convertToTitle(n)