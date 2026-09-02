class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n1 = len(s)
        n2 = len(t)
        lastFoundIndex = -1
        for i in range(n1):
            found = False
            for j in range(lastFoundIndex+1, n2):
                print(s[i], t[j])
                if s[i] == t[j]:
                    found = True
                    lastFoundIndex = j
                    break
            if found == False:
                return False

        return True