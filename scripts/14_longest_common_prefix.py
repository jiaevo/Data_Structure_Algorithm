 def longestCommonPrefix(strs: List[str]) -> str:
     if not strs:
         return ""
     for i, strgroup in enumerate(zip(*strs)):
         if len(set(strgroup)) > 1:
             return strs[0][:i]
         else:
             return min(str)