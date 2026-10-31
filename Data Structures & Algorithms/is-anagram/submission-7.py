class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        if sorted(s) == sorted(t): #O(n log n + m log m)
            return True

        return False
        