def get_max(left,right,s):
    while left >= 0 and right <= len(s)-1:
        # print(left)
        # print(right)
        if s[left] == s[right]:
            left = left - 1
            right = right + 1
        else:
            break
    return right - left - 1

def longestpalindromic(s):
    pad_len = 0
    start_pos = 0
    for i in range(0,len(s)):
        print('current iteration:{}'.format(i))
        print('current position:{}'.format(start_pos))
        if i < len(s) -2:
            sub_len = max(get_max(i,i,s),get_max(i,i+1,s))
            print('max sub len:{}'.format(sub_len))
            if sub_len > pad_len:
                pad_len = sub_len
                start_pos = int(i - (pad_len-1)/2)
                print('updated position:{}'.format(start_pos))
    return s[start_pos:start_pos + pad_len]