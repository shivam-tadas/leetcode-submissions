class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        self.possible = False
        
        def SetPartBT(curr: List[int], remain: List[int], start: int) -> None:
            if remain == []:
                return

            currProd = 1
            remainProd = 1

            for i in curr:
                if i == 0:
                    continue
                currProd *= i

            for i in remain:
                if i == 0:
                    continue
                remainProd *= i

            if currProd == remainProd:
                if currProd == target:
                    self.possible = True
                return

            for i in range(start, len(remain)):
                tmp = remain[i]
                remain[i] = 0
                SetPartBT(curr + [tmp], remain, i+1)
                remain[i] = tmp

        SetPartBT([], nums, 0)
        return self.possible