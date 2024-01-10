class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        start = 0
        while start <= len(haystack)-len(needle):
            if haystack[start] == needle[0] and haystack[start:start + len(needle)] == needle:
                return start
            start+=1
        return -1
                
        