class Solution:

    #  2#s#3#lol
    #      i

    # [s#, ]
    def encode(self, strs: List[str]) -> str:
        encoded_str = []

        for word in strs: #O(word)
            encoded_word = f'{len(word)}#{word}'
            encoded_str.append(encoded_word)      
        return ''.join(encoded_str)

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        i = 0

        while i < len(s): #O(s)
            size = ""
            while s[i] != '#':
                size += s[i]
                i += 1
            size = int(size)
            word = s[i+1:i+1+size]
            decoded_list.append(word)
            i += 1+size
        
        return decoded_list
