# coding=utf-8
"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
"""


class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        def generate(numRows):

            if numRows == 0:
                return []
            res = [[1]]
            if numRows == 1:
                return res
            res = [[1], [1, 1]]
            if numRows == 2:
                return res

            for i in range(numRows - 2):
                temp = [1]
                for j in range(len(res[-1]) - 1):
                    temp.append(res[-1][j] + res[-1][j + 1])
                temp.append(1)
                res.append(temp)
            return res

        while rowIndex <= 33 and rowIndex >= 0:
            res = generate(rowIndex + 1)
            print(res[rowIndex])
            return res[rowIndex]


if __name__ == '__main__':

    rowIndex = 3
    solution = Solution()
    solution.getRow(rowIndex)