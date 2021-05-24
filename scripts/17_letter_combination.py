# dfs using recursive to iterate all char in the string when reach the length of string return
L = {'1':"",'2':"abc",'3':"def",'4':"ghi",'5':"jkl",
     '6':"mno",'7':"pqrs",'8':"tuv",'9':"wxyz"}

def lettercomb(digits):
    total_len = len(digits)
    ans = []
    if digits =='':
        return []
    def dfs_word(letter,pos):
        print(total_len)
        if pos == total_len:
            return ans.append(letter)
        else:
            mapped_letters = L[digits[pos]]
            if len(mapped_letters) == 0:
                dfs_word(letter,pos+1)
            else:
                for i in mapped_letters:
                    dfs_word(letter+i,pos+1)
    dfs_word('',0)
    return ans


