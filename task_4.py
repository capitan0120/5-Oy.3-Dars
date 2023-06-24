class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1):
            s = ''
            for j in range(i, len(needle)+i):
                s += haystack[j]
            if needle == s:
                return i
        return -1