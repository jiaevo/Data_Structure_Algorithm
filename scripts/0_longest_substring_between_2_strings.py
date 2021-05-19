def longest(X,Y):
    dp = [[0 for k in range(len(X))] for l in range(len(Y))]
    result = 0
    for i in range(len(X)):
        for j in range(len(Y)):
            if(i == 0 or j == 0):
                dp[i][j] = 0
            elif(X[i] == Y[j]):
                dp[i][j] = dp[i-1][j-1] + 1
                result = max(result, dp[i][j])
            else:
                dp[i][j] = 0
    return result

X = 'OldSite:GeeksforGeeks.org'
Y = 'NewSite:GeeksQuiz.com'
longest(X,Y)