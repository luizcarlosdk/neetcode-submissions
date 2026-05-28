from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        frequency = [[] for i in range(len(nums) + 1)]
        answer = []

        for num in nums:
            count[num] += 1
        for num, count in count.items():
            frequency[count].append(num)

        for i in range(len(frequency) - 1, 0, -1):
            for num in frequency[i]:
                answer.append(num)
                if len(answer) == k:
                    return answer

        