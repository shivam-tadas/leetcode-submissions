class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = list(map(int, version1.split('.')))
        version2 = list(map(int, version2.split('.')))

        for i in range(min(len(version1), len(version2))):
            if version1[i] > version2[i]:
                return 1

            if version2[i] > version1[i]:
                return -1

        if len(version1) > len(version2):
            for i in range(len(version2), len(version1)):
                if version1[i] > 0:
                    return 1

        elif len(version2) > len(version1):
            for i in range(len(version1), len(version2)):
                if version2[i] > 0:
                    return -1

        return 0