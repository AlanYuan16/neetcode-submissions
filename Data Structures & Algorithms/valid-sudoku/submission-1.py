class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        col = defaultdict(set)
        square = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                val = board[r][c]
                if (val in row[r] or val in col[c] or val in square[r//3, c//3]):
                    return False
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                square[(r//3, c//3)].add(board[r][c])
        return True



