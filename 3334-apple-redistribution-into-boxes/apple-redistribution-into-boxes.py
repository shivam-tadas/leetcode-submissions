class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        apples = sum(apple)
        capacity.sort(reverse=True)
        i = 0
        totalCapacity = 0
        for i in range(len(capacity)):
            totalCapacity += capacity[i]
            if totalCapacity >= apples:
                break

        return i+1