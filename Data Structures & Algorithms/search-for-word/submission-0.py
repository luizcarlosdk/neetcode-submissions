
# A B C D
# S A A T
# A C A E

# [] word -> False
# uppercase english letters in board and word?
# max size of the board

# hashset = (row, col)

# 

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # up right down left
        path = set()

        def dfs(r, c, i):
            if i == len(word):
                return True
            
            if (min(r,c) < 0 or
            r >= rows or c >= cols or
            board[r][c] != word[i] or
            (r, c) in path
            ):
                return False

            path.add((r, c))
            
            res = (
                dfs(r + directions[0][0], c + directions[0][1], i+1) or
                dfs(r + directions[1][0], c + directions[1][1], i+1) or
                dfs(r + directions[2][0], c + directions[2][1], i+1) or
                dfs(r + directions[3][0], c + directions[3][1], i+1)
            )
            path.remove((r, c))
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r, c, 0):
                    return True
        
        return False
        
