# coding=utf-8
"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # 前 3 种情况比较特殊
        if numRows == 0:
            return []

        res = [[1]]
        if numRows == 1:
            return res

        res = [[1], [1, 1]]
        if numRows == 2:
            return res


        for i in range(numRows-2):
            temp = [1]
            # res[-1] 表示前一个 list，第一次为 [1,1]
            for j in range(len(res[-1])-1):
                # 相加得到需要的数据
                temp.append(res[-1][j]+res[-1][j+1])
            # 添加末尾的 1
            temp.append(1)
            # 结果再添加上新生成的 list
            res.append(temp)
        print(res)
        return res



if __name__ == '__main__':

    numRows = 5
    solution = Solution()
    solution.generate(numRows)