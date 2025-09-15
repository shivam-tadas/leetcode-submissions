class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        count = 0
        words = text.split(' ')
        for word in words:
            canBeTyped = True
            for c in word:
                if c in brokenLetters:
                    canBeTyped = False
                    break
            if canBeTyped:
                count += 1
        return count           