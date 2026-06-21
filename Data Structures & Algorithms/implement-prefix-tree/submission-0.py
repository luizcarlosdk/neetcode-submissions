class TrieNode:
    def __init__(self):
        self.is_end = False
        self.pos = [None]*26

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if curr.pos[idx] != None:
                curr = curr.pos[idx]
            else:
                curr.pos[idx] = TrieNode()
                curr = curr.pos[idx]
        curr.is_end = True

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if curr.pos[idx] == None:
                return False
            curr = curr.pos[idx]
        return curr.is_end
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            idx = ord(char) - ord('a')
            if curr.pos[idx] == None:
                return False
            curr = curr.pos[idx]
        return True
        
        