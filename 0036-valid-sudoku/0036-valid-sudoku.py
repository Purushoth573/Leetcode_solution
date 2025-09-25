from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for i in range(9):
            s = set()
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in s:
                        return False
                    s.add(board[i][j])
        
        # Check columns
        for j in range(9):
            s = set()
            for i in range(9):
                if board[i][j] != ".":
                    if board[i][j] in s:
                        return False
                    s.add(board[i][j])
        
        # Check 3x3 sub-boxes
        for box_row in [0, 3, 6]:
            for box_col in [0, 3, 6]:
                s = set()
                for i in range(box_row, box_row + 3):
                    for j in range(box_col, box_col + 3):
                        if board[i][j] != ".":
                            if board[i][j] in s:
                                return False
                            s.add(board[i][j])
        
        return True
