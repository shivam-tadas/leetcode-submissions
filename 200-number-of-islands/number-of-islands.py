class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        islands = 0
        visited = set()

        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and grid[i][j] == '1':
                    islands += 1
                    bfsQueue = deque([(i, j)])

                    while bfsQueue:
                        currI, currJ = bfsQueue.popleft()
                        if (currI, currJ) in visited:
                            continue

                        visited.add((currI, currJ))

                        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            newJ = currJ + dx
                            newI = currI + dy

                            if -1 < newI < m and -1 < newJ < n and (newI, newJ) not in visited and grid[newI][newJ] == '1':
                                bfsQueue.append((newI, newJ))

        return islands