class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
    
    def add_word(self, word):
        curr = self
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res, visited = set(), set()
        ROWS, COLS = len(board), len(board[0])
        root = TrieNode()

        for word in words:
            root.add_word(word)

        def dfs(r, c, node, word):
            if (
                min(r, c) < 0 or
                r >= ROWS or
                c >= COLS or
                board[r][c] not in node.children or
                (r, c) in visited
            ):
                return
            
            visited.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.is_word:
                res.add(word)

            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r + 1, c, node, word)
            dfs(r, c - 1, node, word)
            visited.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")
        
        return list(res)