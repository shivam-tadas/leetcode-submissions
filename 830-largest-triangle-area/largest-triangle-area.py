class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        max_area = 0
        n = len(points)

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    x1, y1 = points[i][0], points[i][1]
                    x2, y2 = points[j][0], points[j][1]
                    x3, y3 = points[k][0], points[k][1]

                    new_area = 0.5 * abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))
                    max_area = max(new_area, max_area)

        return max_area