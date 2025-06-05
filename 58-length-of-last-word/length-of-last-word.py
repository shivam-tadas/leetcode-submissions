class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.replace('  ', ' ')
        return len(s.split()[-1])