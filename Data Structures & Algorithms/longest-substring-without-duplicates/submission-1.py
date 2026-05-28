class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        seen = {}
        max_window_size = 0

        for idx in range(len(s)):
            char = s[idx]
            if char in seen:
                start = max(start, seen[char] + 1)
            
            seen[char] = idx
            window_size = idx - start + 1
            max_window_size = max(max_window_size, window_size)

        return max_window_size 