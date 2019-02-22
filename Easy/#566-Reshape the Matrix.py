"""
In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one 
with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing 
the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing
 order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; 
Otherwise, output the original matrix.

Example 1:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 1, c = 4
Output: 
[[1,2,3,4]]
Explanation:
The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
Example 2:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 2, c = 4
Output: 
[[1,2],
 [3,4]]
Explanation:
There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.
Note:
The height and width of the given matrix is in range [1, 100].
The given r and c are all positive.
"""
class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        """方法一：使用蛮力
        if r >= len(nums) and c >= len(nums[0]):
            return nums
        # 转换成行向量
        one_row = [nums[i][j] for i in range(len(nums)) for j in range(len(nums[i]))]
        # 重新整合形状
        new_nums = [one_row[c*i:c*i+c] for i in range(r)]

        return new_nums
        """
        # 方法二：使用队列
        import collections

        d = collections.deque(sum(nums, []))
        if r*c != len(nums)*len(nums[0]):
            return nums

        return [[d.popleft() for i in range(c)] for j in range(r)]

if __name__ == "__main__":

    # nums = [[1, 2], [3, 4]]
    nums = [[1, 2], [3, 4], [5, 6]]
    r = 2
    c = 3
    solution = Solution()
    print(solution.matrixReshape(nums, r, c))