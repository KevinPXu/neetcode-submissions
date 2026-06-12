class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]
        boxes = [[False] * 9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    boxIdx = (i // 3) * 3 + (j // 3)
                    num = ord(board[i][j]) - ord("1")
                    if rows[i][num] or cols[j][num] or boxes[boxIdx][num]:
                        return False
                    rows[i][num] = cols[j][num] = boxes[boxIdx][num] = True
        return True