class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str: 
        ans = ""

        for i in range(len(strs[0])):
            for word in strs:
                if i == len(word) or word[i] != strs[0][i]:
                    return ans
            ans += word[i]
        
        return ans



# so, i receive an array of strs, and return the longest common prefix of them all
# so to check the common prefix, we need to check all of them in the same index, seing if all of them have
# the same letter, but we need to be careful cause they could not be the same size