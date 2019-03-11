"""
Given a binary matrix A, we want to flip the image horizontally, then invert it, and return 
the resulting image.

To flip an image horizontally means that each row of the image is reversed.  For example, 
flipping [1, 1, 0] horizontally results in [0, 1, 1].

To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. 
For example, inverting [0, 1, 1] results in [1, 0, 0].

Example 1:

Input: [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]
Explanation: First reverse each row: [[0,1,1],[1,0,1],[0,0,0]].
Then, invert the image: [[1,0,0],[0,1,0],[1,1,1]]
Example 2:

Input: [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
Output: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]].
Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
Notes:

1 <= A.length = A[0].length <= 20
0 <= A[i][j] <= 1
"""
import numpy as np
class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        # 逆转矩阵的每行
        A_rev = []
        for row in A:
            row_rev = row[::-1]
            A_rev.append(row_rev)

        # 矩阵取反
        ans = []
        for row in A_rev:
            for val in row:
                if val == 0:
                    val = 1
                else: 
                    val = 0
                ans.append(val)
        # 转换回 list 类型
        ans = np.array(ans).reshape(np.array(A).shape).tolist()

        return ans

if __name__ == "__main__":

    A = [[1,1,0],[1,0,1],[0,0,0]]
    # A = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
    solution = Solution()
    print(solution.flipAndInvertImage(A))