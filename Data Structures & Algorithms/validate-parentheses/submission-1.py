class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        valid_brackets = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }

        for c in s:
            if not stack and c in valid_brackets.values():
                return False
            elif c in valid_brackets.keys():
                stack.append(c)
            else:
                last_bracket = stack.pop()

                if valid_brackets[last_bracket] != c:
                    return False
        
        if stack:
            return False
        return True
                    
