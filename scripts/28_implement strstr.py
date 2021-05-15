def strStr(haystack,needle):
    for i in range(len(haystack)):
        # print(i)
        if needle[0] == haystack[i]:
            
            k = i
            # print(k)
            match = True
            for j in range(len(needle)):
                if needle[j] != haystack[k]:
                    match = False
                    break
                if k == len(haystack) - 1 and j < len(needle) -1:
                    match = False
                    break
                k = k+1
            #     print(match)
            # print(match)
            if match == True:
                return i
    return -1



