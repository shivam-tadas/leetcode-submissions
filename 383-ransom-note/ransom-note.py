class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        alphabets = {}

        for i in range(len(magazine)):
            if magazine[i] not in alphabets.keys():
                alphabets[magazine[i]] = 1
            else:
                alphabets[magazine[i]] = alphabets[magazine[i]] + 1
                
        for i in ransomNote:
            if i not in alphabets.keys() or alphabets[i] == 0:
                return False

            alphabets[i] -= 1
            print(alphabets)

        return True