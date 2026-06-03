class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        stack = []

        for bracket in s:
            if bracket in hashmap.values():
                stack.append(bracket)
                continue
            else:
                if len(stack) == 0 or stack.pop() != hashmap[bracket]:
                    return False
                
        
        if len(stack) > 0:
            return False
        return True
