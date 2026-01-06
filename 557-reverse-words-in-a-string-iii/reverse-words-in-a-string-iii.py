class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        n = len(s)
        start = 0
        end = 0
        for i in range(n):
            if s[i] == ' ':
                while start < end:
                    s[start], s[end] = s[end], s[start]
                    start += 1
                    end -= 1

                start = i+1

            end = i

        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

        return ''.join(s)