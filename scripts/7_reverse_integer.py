def reverse(x: int) -> int:
    negative_ind = False
    if x < 0:
        negative_ind = True
        x = x*-1
    
    rev = 0
    while x:
        mod = x % 10
        x = round(x / 10)
        rev = rev*10 + mod
    if negative_ind == True:
        rev = rev * -1
    return rev
        