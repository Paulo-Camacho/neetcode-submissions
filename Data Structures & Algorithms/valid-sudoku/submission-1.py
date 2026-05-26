class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # We are going to use a hashset
        # We need to keep track of 
        # 'row', row_index, value
        # 'col', col_index, value
        # 'box', row_index, col_index, value
        # Start at 05-21-26 @3:53PM

        seen = set()

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == '.':
                    continue
                row_key = ('row', row, board[row][col])
                col_key = ('col', col, board[row][col])
                # Remember to define what box we are in
                box_key = ('box', row // 3, col // 3, board[row][col])
                if row_key in seen or col_key in seen or box_key in seen:
                    return False
                else:
                    seen.add(row_key)
                    seen.add(col_key)
                    seen.add(box_key)
        print(seen)
        return True 