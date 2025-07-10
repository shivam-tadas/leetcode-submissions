class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == '' or needle == haystack:
            return 0
        i = 0
        while i < len(haystack):
            if haystack[i] == needle[0] and i + len(needle) <= len(haystack):
                if len(needle) == 1:
                    return i
                j = 1
                while j < len(needle):
                    if haystack[i+j] != needle[j]:
                        break
                    if j == len(needle) - 1:
                        return i
                    j += 1
            i += 1
        return -1