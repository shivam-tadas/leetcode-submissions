class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False

        vowel = 'aeiouAEIOU'
        consonant = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
        digit = '0123456789'
        vowels = consonants = digits = 0
        for ch in word:
            if ch in vowel:
                vowels += 1
            elif ch in consonant:
                consonants += 1
            elif ch in digit:
                digits += 1
            else:
                return False

        if vowels == 0 or consonants == 0:
            return False

        return True