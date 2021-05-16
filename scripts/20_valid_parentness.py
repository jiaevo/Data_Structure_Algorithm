#use stack to last in first out 
def valid_parentness(strs):
    stk = []
    right = {'}':1,']':1,')':1}
    left = {'{':1,'[':1,'(':1}
    valid_flag = True

    for i,j in enumerate(strs):
        if len(stk) == 0 and j in right.keys():
            valid_flag = False
            break
        elif j in right.keys():
            if stk[0] == '(' and j == ')':
                stk.pop(0)
            elif stk[0] == '{' and j == '}':
                stk.pop(0)
            elif stk[0] == '[' and j == ']':
                stk.pop(0)
            else:
                valid_flag = False
                break           
        if j in left.keys():
            stk.insert(0,j)
    if len(stk) > 0:
        valid_flag = False
    
    return valid_flag
        
