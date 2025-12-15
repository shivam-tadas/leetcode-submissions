class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        min_operations = float('inf')
        for i in range(len(blocks)-k+1):
            recolors = 0
            for j in range(i, i+k):
                if blocks[j] == 'W':
                    recolors += 1

            min_operations = min(min_operations, recolors)

        return min_operations