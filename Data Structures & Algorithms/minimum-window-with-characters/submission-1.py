
# t empty
# anything different than english letters?
# just uppercase and lowercase english letters

# OUZODYXAZV
# 
# XYZ

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_map, window_map = defaultdict(int), defaultdict(int)
        l, have = 0, 0
        output = ''
        min_len = float('inf')

        for char in t:
            t_map[char] += 1
        need = len(t_map)

        for r in range(len(s)):
            char = s[r]
            window_map[char] += 1

            if window_map[char] == t_map[char]:
                have += 1
            
            while need == have and l <= r:
                char = s[l]
                if (r-l+1) < min_len:
                    min_len = (r-l+1)
                    output = s[l:r+1]
                window_map[char] -= 1
                if char in t_map and window_map[char] < t_map[char]:
                    have -= 1
                l += 1

        return output
                
