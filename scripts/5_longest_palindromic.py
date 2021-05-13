def get_max(left,right,s):
    while s[left] == s[right] and s[left] >= 0 and s[right] <= len(s)-1:
        left = left - 1
        right = right + 1
    
    return right - left - 1

def longestpalindromic(s):
    pad_len = 0
    start_pos = 0
    for i in range(0,len(s)):
        sub_len = max(get_max(i,i,s),get_max(i,i+1,s))
        if sub_len > pad_len:
            pad_len = sub_len
            start_pos = i - (start_pos-1)/2

    return s[start_pos:start_pos + pad_len]