class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq_per_pattern = defaultdict(list)

        for word in strs:
            count = [0]*26

            for letter in word:
                position = ord(letter) - ord("a")
                count[position] += 1

            freq_per_pattern[tuple(count)].append(word)
        
        return list(freq_per_pattern.values())

        