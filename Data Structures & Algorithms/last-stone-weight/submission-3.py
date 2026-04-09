class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap = [-s for s in stones]
        heapq.heapify(minHeap)
        while len(minHeap) > 1:
            stone1 = heapq.heappop(minHeap) # -7
            stone2 = heapq.heappop(minHeap) # -6

            if (stone1 < stone2):
                heapq.heappush(minHeap, stone1 - stone2)
        return -minHeap[0] if minHeap else 0



