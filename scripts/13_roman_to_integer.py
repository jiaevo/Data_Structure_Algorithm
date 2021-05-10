def romanToInt(s: str) -> int:
    str_len = len(s)
    look_next = False
    num = 0
    for i in range(0,str_len):
        if look_next == True:
            look_next = False
            continue
        if s[i] == 'I':
            if i < str_len - 1:
                if s[i+1] == 'V':
                    num = num + 4
                    look_next = True
                elif s[i+1] == 'X':
                    num = num + 9
                    look_next = True
                else:
                    num = num + 1
                    look_next = False
            else:
                num = num + 1
                look_next = False
        
        elif s[i] == 'X':
            if i < str_len - 1:
                if s[i+1] == 'L':
                    num = num + 40
                    look_next = True
                elif s[i+1] == 'C':
                    num = num + 90
                    look_next = True
                else:
                    num = num + 10
                    look_next = False
            else:
                num = num + 10
                look_next = False
        
        elif s[i] == 'C':
            if i < str_len -1:
                if s[i+1] == 'D':
                    num = num + 400
                    look_next = True
                elif s[i+1] == 'M':
                    num = num + 900
                    look_next = True
                else:
                    num = num + 100
                    look_next = False
            else:
                num = num + 100
                look_next = False
        elif s[i] == 'V':
            num = num + 5
            look_next = False
        elif s[i] == 'L':
            num = num + 50
            look_next = False
        elif s[i] == 'D':
            num = num + 500
            look_next = False
        elif s[i] == 'M':
            num = num + 1000
            look_next = False
       
    return num