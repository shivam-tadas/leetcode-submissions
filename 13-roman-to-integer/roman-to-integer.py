class Solution:
    def romanToInt(self, s: str) -> int:
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        num = 0

        i = len(s) - 1
        while i >= 0:
            if i == 0:
                num += values[s[i]]
                i -= 1
                continue

            if values[s[i]] > values[s[i-1]]:
                num += values[s[i]] - values[s[i-1]]
                print("in 'if'", values[s[i]] - values[s[i-1]])
                i -= 1
            else:
                num += values[s[i]]
                
            print(i, num)
            i -= 1

        return num