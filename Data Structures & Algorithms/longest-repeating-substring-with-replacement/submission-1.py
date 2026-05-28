class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        frequency_dict = defaultdict(int)
        output=0

        for r in range(len(s)):
            frequency_dict[s[r]] += 1

            while (r-l+1) - max(frequency_dict.values()) > k:
                frequency_dict[s[l]] -= 1
                l += 1


            output = max(output, r-l+1)
        
        return output






