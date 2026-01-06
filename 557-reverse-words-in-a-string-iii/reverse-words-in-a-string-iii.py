class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        for i in range(len(words)):
            words[i] = words[i][::-1]
        
        ans = ''
        for word in words:
            ans += ' ' + word

        return ans[1:]