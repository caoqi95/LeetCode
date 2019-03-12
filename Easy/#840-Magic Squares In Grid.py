"""
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).

 

Example 1:

Input: [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]
Output: 1
Explanation: 
The following subgrid is a 3 x 3 magic square:
438
951
276

while this one is not:
384
519
762

In total, there is only one magic square inside the given grid.
Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
0 <= grid[i][j] <= 15
"""
class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        magicCount = 0
        for i in range(0, len(grid)-2):
            for j in range(0, len(grid[0])-2):
                if self.isMagic(grid, i, j):
                    magicCount += 1
        return magicCount
    
    def isMagic(self, grid, i, j):
        sum = grid[i][j] + grid[i][j+1] + grid[i][j+2]

        # row check
        for r in range(i, i+3):
            if sum != grid[r][j] + grid[r][j+1] + grid[r][j+2]:
                return False
        
        # column check
        for c in range(j, j+3):
            if sum != grid[i][c] + grid[i+1][c] + grid[i+2][c]:
                return False

        # diagonal check 1
        if sum != grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2]:
            return False

        # diagonal check 2
        if sum != grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j]:
            return False
        
        # distinct check
        digitMap = {}
        for r in range(i, i+3):
            for c in range(j, j+3):
                if grid[r][c] not in digitMap and grid[r][c] < 10 and grid[r][c] > 0:
                    digitMap[grid[r][c]] = True
                else:
                    return False
        
        return True

if __name__ == "__main__":

    grid = [[4,3,8,4], [9,5,1,9], [2,7,6,2]]
    solution = Solution()
    print(solution.numMagicSquaresInside(grid))