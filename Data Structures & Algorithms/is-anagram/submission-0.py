class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        anagramDict = defaultdict(int)

        for char in s:
            anagramDict[char] += 1
        
        for char in t:
            if char in anagramDict and anagramDict[char] > 0:
                anagramDict[char] -= 1
            else:
                return False

        
        return True








        