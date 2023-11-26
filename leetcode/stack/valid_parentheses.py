class Solution:
    def isValid(self, s: str) -> bool:
        paren_stack = []

        parentheses = {')': '(',
                        '}': '{',
                        ']': '['}

        for paren in s:
            if paren in parentheses.values():
                # push
                paren_stack.append(paren)
            else:
                if paren_stack and (paren_stack[-1] == parentheses[paren]):
                    # pop
                    paren_stack.pop()
                else:
                    return False
        
        if paren_stack:
            return False
        else:
            return True
    