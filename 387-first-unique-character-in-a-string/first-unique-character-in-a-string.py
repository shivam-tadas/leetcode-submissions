class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = {}
        for i in range(len(s)):
            if s[i] not in chars:
                chars[s[i]] = 1
            else:
                chars[s[i]] += 1

        print(chars)

        for i in chars:
            if chars[i] == 1:
                print(i)
                return s.find(i)

        return -1