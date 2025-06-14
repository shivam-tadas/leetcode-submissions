class Solution:
    def minMaxDifference(self, num: int) -> int:
        num = str(num)
        firstNonZero = firstNonNine = ''
        maxNum = minNum = ''

        for i in num:
            if i == '9':
                continue

            firstNonNine = i
            break

        for i in num:
            if i == '0':
                continue

            firstNonZero = i
            break

        for i in num:
            if i == firstNonNine:
                maxNum += '9'
            else:
                maxNum += i

        for i in num:
            if i == firstNonZero:
                minNum += '0'
            else:
                minNum += i

        return int(maxNum) - int(minNum)
