from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if "" in strs:
            return ""
        if len(strs) == 1:
            return strs[0]
        s = min(strs, key=len)
        i = 0 
        while i < len(s):
            for str in strs:
                if str[i] != s[i]:
                    return s[:i]
            i += 1
        return s[:i]        
        