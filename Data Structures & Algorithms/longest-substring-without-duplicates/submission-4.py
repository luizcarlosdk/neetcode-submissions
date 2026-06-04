class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_size = 0
        l, r = 0, 0
        char_set = set()

        while r < len(s):

            if s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            else:
                char_set.add(s[r])
                max_size = max(max_size, len(char_set))
                r += 1
        
        return max_size

#

# entry empty = 0
# Zz duplicated?