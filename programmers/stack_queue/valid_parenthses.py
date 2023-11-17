def solution(s):
    empty_stack = []
    for paren in s:
        if paren == '(':
            empty_stack.append(paren)
        else:
            if empty_stack:
                empty_stack.pop()
            else:
                return False
            
    if empty_stack:
        return False
    else: 
        return True
    
    
                