class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        hasPrefix = False

        for i in range(len(word)):
            if word[i] == ch:
                hasPrefix = True
                break

        if hasPrefix:
            prefix = word[0:i+1]
            word = word[i+1:]
            prefix = prefix[::-1]
            word = prefix + word

        return word