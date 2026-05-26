class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # We are going to use a hashset

        uni = set()
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    continue
                row_key = ("row", row, board[row][col])
                col_key = ('col', col, board[row][col])
                box_key = ('box', row // 3, col // 3, board[row][col])

                if row_key in uni or col_key in uni or box_key in uni:
                    return False
                else:
                    uni.add(row_key)
                    uni.add(col_key)
                    uni.add(box_key)
        return True
                
