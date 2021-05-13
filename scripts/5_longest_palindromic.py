s = "cbbd"
if len(s) % 2 == 0:
    current = len(s)/2 - 1
    next = len(s)/2
    flag = False
    while(next<=len(s)-1):
        if s[current] == s[next]:
            current = current - 1
            next = next + 1
            flag = True
        else:
            flag = False
            break

