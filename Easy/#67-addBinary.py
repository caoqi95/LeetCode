"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

solution from this blog：https://blog.csdn.net/guoziqing506/article/details/51555714
"""
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # 从后往前遍历每个字符串
        index_a = len(a) - 1
        index_b = len(b) - 1
        # 返回的结果
        result = ""
        # 进位
        c = 0
        # 开始遍历
        while index_a >= 0 or index_b >= 0:
            t1 = int(a[index_a]) if index_a >= 0 else 0
            t2 = int(b[index_b]) if index_b >= 0 else 0
            temp = t1 + t2 + c
            result = str(temp % 2) + result  # %：对 temp 进行除 2 取 余数操作，得到单位相加结果
            c = temp // 2  # //：对 temp 进行除 2 取整数商的部分，得到进位
            index_a -= 1  # 往前遍历
            index_b -= 1
        # 如果进位为 1
        if c == 1:
            result = "1" + result

        print(result)
        return result


if __name__ == '__main__':
    a = "1010"
    b = "1011"
    solution = Solution()
    solution.addBinary(a,b)
