"""
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
 

Example 1:

Input:
matrix = [
  [1,2,3,4],
  [5,1,2,3],
  [9,5,1,2]
]
Output: True
Explanation:
In the above grid, the diagonals are:
"[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
In each diagonal all elements are the same, so the answer is True.
Example 2:

Input:
matrix = [
  [1,2],
  [2,2]
]
Output: False
Explanation:
The diagonal "[1, 2]" has different elements.

Note:

matrix will be a 2D array of integers.
matrix will have a number of rows and columns in range [1, 20].
matrix[i][j] will be integers in range [0, 99].
"""
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        groups = {}  # 用于存储对角线上的值
        for r, row in enumerate(matrix):
          for c, val in enumerate(row):
            if r-c not in groups: # 如果 r-c 不存在，则增加其和其对应的值
              groups[r-c] = val
            elif groups[r-c] != val: # 如果 r-c 对应的值与原有的值不符，则返回 False
              return False
            
        return True

if __name__ == "__main__":

    matrix = [[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]]  # return True
    # matrix = [[1, 2], [2, 2]]  # return False
    solution = Solution()
    print(solution.isToeplitzMatrix(matrix))