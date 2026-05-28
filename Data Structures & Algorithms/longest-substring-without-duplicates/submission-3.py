class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        max_len, left = 0, 0

        for char in s:
            while char in unique:
                unique.remove(s[left])
                left += 1
            unique.add(char)
            max_len = max(len(unique), max_len)
        
        return max_len