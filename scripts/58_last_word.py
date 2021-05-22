def lengthlastword(s):
    last_word_len = 0
    for i in range(len(s)):
        if s[len(s)-1-i] != ' ':
            last_word_len = last_word_len +1
        elif s[len(s)-1-i] == ' ':
            break
    return last_word_len

        