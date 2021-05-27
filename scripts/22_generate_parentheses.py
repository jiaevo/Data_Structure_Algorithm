def generateuntil(left, right, curr_string, result):
    if left == 0 and right == 0:
        return result.append(curr_string)
    
    if left > 0:
        generateuntil(left-1,right,curr_string + '(',result)
    if right > left:
        generateuntil(left,right-1,curr_string + ')',result)

def generateParenthesis(n):
    result = []
    generateuntil(n,n,"",result)
    return result


