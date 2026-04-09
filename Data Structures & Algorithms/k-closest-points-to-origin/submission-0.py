class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            x, y = point
            distance = -math.sqrt((0 - x) ** 2 + (0 - y) ** 2)
            heapq.heappush(heap, [distance, x, y])

            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for dist, x, y in heap:
            res.append([x,y])

        return res 