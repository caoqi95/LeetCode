"""
On an 8 x 8 chessboard, there is one white rook.  There also may be empty squares, white bishops, and black pawns.  These are given as characters 'R', '.', 'B', and 'p' respectively. Uppercase characters represent white pieces, and lowercase characters represent black pieces.

The rook moves as in the rules of Chess: it chooses one of four cardinal directions (north, east, west, and south), then moves in that direction until it chooses to stop, reaches the edge of the board, or captures an opposite colored pawn by moving to the same square it occupies.  Also, rooks cannot move into the same square as other friendly bishops.

Return the number of pawns the rook can capture in one move.

Example 1:
Input: [[".",".",".",".",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        [".",".",".","R",".",".",".","p"],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."]]
Output: 3
Explanation: 
In this example the rook is able to capture all the pawns.

Example 2:
Input: [[".",".",".",".",".",".",".","."],
        [".","p","p","p","p","p",".","."],
        [".","p","p","B","p","p",".","."],
        [".","p","B","R","B","p",".","."],
        [".","p","p","B","p","p",".","."],
        [".","p","p","p","p","p",".","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".","."]]
Output: 0
Explanation: 
Bishops are blocking the rook to capture any pawn.

Example 3:
Input: [[".",".",".",".",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        ["p","p",".","R",".","p","B","."],
        [".",".",".",".",".",".",".","."],
        [".",".",".","B",".",".",".","."],
        [".",".",".","p",".",".",".","."],
        [".",".",".",".",".",".",".","."]]
Output: 3
Explanation: 
The rook can capture the pawns at positions b5, d6 and f5.
"""
import numpy as np
class Solution(object):
    def numRookCaptures(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """

        count = 0

        # finding Rook's position
        board = np.array(board)
        x, y = np.where(board == 'R')[0][0], np.where(board == 'R')[1][0]

        # for four directions
        if x < 7:
            for k in range(x+1, 8): # in right direction, y will remain same
                if board[k][y] == 'p':
                    count += 1
                    print("right")
                    break
                elif board[k][y] != '.':
                    break
            
        if y < 7:
            for k in range(y+1, 8): # in bottom direction, x will remain same
                if board[x][k] == 'p':
                    count += 1
                    print("bottom")
                    break
                elif board[x][k] != '.':
                    break
        if x > 0:
            for k in range(x-1, -1, -1): # in left direction, y will remain same
                if board[k][y] == 'p':
                    count += 1
                    print("left")
                    break
                elif board[k][y] != '.':
                    break
        if y > 0:
            for k in range(y-1, -1, -1): # in top direction, x will remain same
                if board[x][k] == 'p':
                    count += 1
                    print("top")
                    break
                elif board[x][k] != '.':
                    break
        
        return count


if __name__ == "__main__":

    """
    inputs = [[".",".",".",".",".",".",".","."],
              [".",".",".","p",".",".",".","."],
              [".",".",".","R",".",".",".","p"],
              [".",".",".",".",".",".",".","."],
              [".",".",".",".",".",".",".","."],
              [".",".",".","p",".",".",".","."],
              [".",".",".",".",".",".",".","."],
              [".",".",".",".",".",".",".","."]]
    """
    inputs = [[".",".",".",".",".",".",".","."],
              [".","p","p","p","p","p",".","."],
              [".","p","p","B","p","p",".","."],
              [".","p","B","R","B","p",".","."],
              [".","p","p","B","p","p",".","."],
              [".","p","p","p","p","p",".","."],
              [".",".",".",".",".",".",".","."],
             [".",".",".",".",".",".",".","."]]
    
    """
    inputs = [[".",".",".",".",".",".",".","."],
              [".",".",".","p",".",".",".","."],
              [".",".",".","p",".",".",".","."],
              ["p","p",".","R",".","p","B","."],
              [".",".",".",".",".",".",".","."],
              [".",".",".","B",".",".",".","."],
              [".",".",".","p",".",".",".","."],
              [".",".",".",".",".",".",".","."]]            
    """
    solution = Solution()
    print(solution.numRookCaptures(inputs))

