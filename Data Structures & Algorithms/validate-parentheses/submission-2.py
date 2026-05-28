class Solution:
    def isValid(self, s: str) -> bool:
        
        stack = []
        close_to_open = {
            "(" : ")",
            "{" : "}",
            "[" : "]"
        }

        for c in s:
            if not stack and c in close_to_open.values():
                return False
            elif c in close_to_open.keys():
                stack.append(c)
            else:
                last_bracket = stack.pop()

                if close_to_open[last_bracket] != c:
                    return False
        
        if stack:
            return False
        return True
                    
