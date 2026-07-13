class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column_count = [{} for _ in range(9)]
        square_count = [{} for _ in range(9)]
        for i in range(len(board)):
            row_count = {}
            for j in range(len(board)):
                square_index = (j//3) + (i//3)*3
                current_num = board[i][j]
                if current_num in row_count and current_num != '.':
                    return False
                elif current_num in column_count[j] and current_num != '.':
                    return False
                elif current_num in square_count[square_index] and current_num != '.':
                    return False
                else:
                    row_count[current_num] = 1
                    column_count[j][current_num] = 1
                    square_count[square_index][current_num] = 1
        return True