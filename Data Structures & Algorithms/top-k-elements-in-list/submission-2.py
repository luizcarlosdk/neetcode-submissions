from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        min_heap, output = [], []

        # build frequency
        for num in nums:
            count[num] += 1
        # build min_heap
        for num, freq in count.items():
            heapq.heappush(min_heap, (freq,num))
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        for _ , num in min_heap:
            output.append(num)
        
        return output