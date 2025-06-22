class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        groups = []
        ls = 0
        subStr = ''

        for i in s:
            if ls < k:  # Create group
                subStr += i
                ls += 1
            else:   # Finish creating this group
                ls = 1
                groups.append(subStr)
                subStr = i

        groups.append(subStr)   # Add last group
        if groups and len(groups[-1]) < k:
            groups[-1] += fill * (k - len(groups[-1]))

        return groups