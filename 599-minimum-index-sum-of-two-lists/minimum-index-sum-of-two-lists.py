class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common_strings = []
        for i in range(len(list1)):
            for j in range(len(list2)):
                if list1[i] == list2[j]:
                    common_strings.append((list1[i], i+j))

        least_index_sum = len(list1) + len(list2)
        for i in common_strings:
            least_index_sum = min(least_index_sum, i[1])

        ans = []
        for i in common_strings:
            if i[1] == least_index_sum:
                ans.append(i[0])

        return ans