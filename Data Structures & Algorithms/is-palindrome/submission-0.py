class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = s.lower()
        forward, backwards = 0, len(s) - 1

        while forward < backwards:

            while forward < backwards and not s[forward].isalnum():
                forward += 1
            while forward < backwards and not s[backwards].isalnum():
                backwards -= 1
            
            if s[forward] != s[backwards]:
                return False
            
            forward += 1
            backwards -= 1
        
        return True
