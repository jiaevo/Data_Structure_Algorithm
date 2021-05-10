def lengthOfLongestSubstring(s: str) -> int:
    all_substring = []
    if s == "":
        max_len = 0
    i = 0
    while i < len(s):
        dict_var = {}
        dict_var[s[i]] = 1
        j = i+1
        while j < len(s):
            if s[j] in dict_var.keys():
                break
            else:
                dict_var[s[j]] = 1
                j = j+1
        all_substring.append(len(dict_var))
        i = i+1       
    max_len = max(all_substring)
    
    return max_len

    