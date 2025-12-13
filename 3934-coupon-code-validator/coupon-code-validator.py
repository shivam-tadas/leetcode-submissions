class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        categories = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3
        }
        validChar = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_"
        valid = []
        n = len(code)
        for i in range(n):
            invalid = False
            if code[i] != '' and isActive[i] and businessLine[i] in categories.keys():
                for c in code[i]:
                    if c not in validChar:
                        invalid = True
                        break

                if invalid:
                    break
                
                valid.append((code[i], categories[businessLine[i]]))
        
        print(valid)
        valid.sort(key=lambda x: x[0])
        print(valid)
        valid.sort(key=lambda x: x[1])
        print(valid)
        ans = [i[0] for i in valid]
        return ans
                    