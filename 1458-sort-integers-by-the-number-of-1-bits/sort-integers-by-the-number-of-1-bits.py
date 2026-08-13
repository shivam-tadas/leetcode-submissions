class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        setBits = []

        for i in arr:
            i2 = i
            setBitsCount = 0
            while i2:
                setBitsCount += i2 % 2
                i2 //= 2

            setBits.append((i, setBitsCount))

        ans = []
        setBits = sorted(setBits, key = lambda x: x[1])
        for i in setBits:
            ans.append(i[0])
        
        return ans