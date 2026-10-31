class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_letters = [0]*26

        for a, b in zip(s,t):
            count_letters[ord(a)-ord('a')] += 1
            count_letters[ord(b)-ord('a')] -= 1
        
        
        for val in count_letters:
            if val != 0:
                return False

        return True
        