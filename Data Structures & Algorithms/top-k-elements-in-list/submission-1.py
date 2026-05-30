from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        number_to_count = defaultdict(int)
        sorted_by_freq = []
        output = []

        for num in nums:
            number_to_count[num] += 1
        
        for num, freq in number_to_count.items():
            sorted_by_freq.append([freq, num])

        sorted_by_freq.sort(reverse=True)

        for i in range(k):
            output.append(sorted_by_freq[i][1])
        
        return output