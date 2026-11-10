import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        freq_nums = collections.Counter(nums)
        
        for num, freq in freq_nums.items():
            heapq.heappush(heap, (freq,num))

            if len(heap) > k:
                heapq.heappop(heap)
        
        ans = []

        for _, num in heap:
            ans.append(num)
        
        return ans


# 1 1 2 2 3 3 k = 2? what do i return?
# 2 ways, use a hashmap or minheap by frequency with heap size = k
# O(n log k) # O (n) space