class Solution:
    def reverseWords(self, s: str) -> str:
        curr = ''
        words = []
        for i in s:
            if i == ' ' and curr != '':
                words.append(curr)
                curr = ''
            elif i != ' ':
                curr += i
        words.append(curr)
        print(words)
        newSentence = ''
        for i in words[::-1]:
            if i != ' ' and i != '':
                newSentence += i + ' '
        return newSentence[0:-1:1]