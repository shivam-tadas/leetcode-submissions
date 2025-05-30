class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        mapping = {}

        for i in range(n):
            if s[i] not in mapping.keys():
                if t[i] in mapping.values():
                    return False
                    
                mapping[s[i]] = t[i]

            if t[i] != mapping[s[i]]:
                return False

        return True