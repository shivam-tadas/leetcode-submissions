class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                occurence = {}
                print(s[i:j])
                for k in s[i:j]:
                    if k in occurence:
                        occurence[k] += 1
                    else:
                        occurence[k] = 1
                
                print(occurence)
                if max(occurence.values()) > 2:             
                    break

                ans = max(j-i, ans)

        return ans