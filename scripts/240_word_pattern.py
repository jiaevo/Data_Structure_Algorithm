class Solution:
    def splitword(self,s: str):
        wordlist = []
        word = ''
        for k,j in enumerate(s):
            if j == ' ':
                wordlist.append(word)
                word = ''
                continue
            word = word + j
            if k == len(s)-1:
                wordlist.append(word) 
        return wordlist

    def wordPattern(self, pattern: str, s: str) -> bool:
        wordlist = self.splitword(s)
        lk_pattern = {}
        matched = False
        if len(pattern) != len(wordlist):
            return False
        for i in range(len(wordlist)):
            if pattern[i] not in lk_pattern.keys():
                if wordlist[i] in lk_pattern.values():
                    matched = False
                    break
                else:
                    lk_pattern[pattern[i]] = wordlist[i]
                    matched = True
            else:
                if lk_pattern[pattern[i]] != wordlist[i]:
                    matched = False
                    break
                else:
                    matched = True        
        return matched