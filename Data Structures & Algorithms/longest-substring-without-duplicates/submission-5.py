class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        l, max_sequence = 0, 0

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            max_sequence = max(max_sequence, len(char_set))
        
        return max_sequence

        