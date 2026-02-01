class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_score = sorted(score, reverse=True)
        rank_map = {}
        for i in range(len(score)):
            for j in range(len(sorted_score)):
                if score[i] == sorted_score[j]:
                    rank_map[sorted_score[j]] = j+1
                    break

        answer = []
        for i in score:
            answer.append(str(rank_map[i]))

        print(answer)

        for i in range(len(answer)):
            if answer[i] == '1':
                answer[i] = 'Gold Medal'
            elif answer[i] == '2':
                answer[i] = 'Silver Medal'
            elif answer[i] == '3':
                answer[i] = 'Bronze Medal'

        return answer