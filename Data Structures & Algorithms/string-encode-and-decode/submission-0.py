class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = []
        
        for s in strs:
            encoded_string.append(f'{len(s)}@{s}')

        return "".join(encoded_string)

    def decode(self, s: str) -> List[str]:
        decoded_words = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '@':
                j += 1
            
            length = int(s[i:j])

            i = j + 1
            j = i + length
            word = s[i:j]
            decoded_words.append(word)
            i =j
        
        return decoded_words
            

