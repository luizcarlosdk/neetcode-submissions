class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_freq = defaultdict(int)
        max_seq, max_f = 0, 0

        l = 0
        for r in range(len(s)):
            char_freq[s[r]] += 1
            max_f = max(max_f, char_freq[s[r]])
            
            while (r - l + 1) - max_f > k:
                char_freq[s[l]] -= 1
                l += 1

            max_seq = max(max_seq, r - l + 1)

        return max_seq


# X Y Y X A

# 4 - 2 = 1  > 2
#
#
