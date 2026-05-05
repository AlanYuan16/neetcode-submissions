class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for i in range(9)]
        col = [set() for i in range(9)]
        box = [set() for i in range(9)]

        for r in range(9):
            for c in range(9):
                location = board[r][c]
                box_index = (r // 3) * 3 + (c // 3)

                if location == '.':
                    continue
                else:
                    if location in row[r] or location in col[c] or location in box[box_index]:
                        return False
                row[r].add(location)
                col[c].add(location)
                box[box_index].add(location)
        return True