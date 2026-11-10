class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_count = collections.Counter(nums)
        ans = []

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in freq_count.items():
            buckets[freq].append(num)
        
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                ans.append(num)
            if len(ans) == k:
                break
        
        return ans