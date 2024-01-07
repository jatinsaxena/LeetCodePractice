class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            '}': '{',
            ']' : '[',
            ')' : '('
        }
        
        for character in s:
            if character in mapping.values():
                stack.append(character)
            else:
                if stack:
                    if stack[-1] != mapping[character]:
                        return False
                    
                    stack.pop()
                else:
                    return False
        
        if len(stack)!=0:
            return False
        
        return True
        