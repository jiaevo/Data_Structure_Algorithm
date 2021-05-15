# iterate along pattern string
# if no * after normal char, then just do equality match
# if .* then any char with n times
pos = 0
p = 'abc.*'
s = 'abc'

def regex(p,s):
    dp = [[False for i in range(len(p)+1)] for j in range(len(s)+1)]
    dp[0][0] = False
    for i in range(1,len(p)+1):
        if p[i-1] == '*' and dp[0][i-2] and i > 1:
            dp[0][i] = True
    for i in range(1,len(s)+1):
        for j in range(1,len(p)+1):
            if s[i-1] == p[j-1] or p[j-1] == '.':
                dp[i][j] = dp[i-1][j-1]
            elif p[j-1] == '*':
                if dp[i][j-2]:
                    dp[i][j] = True
                elif dp[i-1][j] and (s[i-1] == p[j-2] or p[j-2] == '.'):
                    dp[i][j] = True
    return dp[i-1][j-1]