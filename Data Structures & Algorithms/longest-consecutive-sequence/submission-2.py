class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_seq = 0

        for num in num_set:
            if num - 1 not in num_set:
                streak = 1
                i = 1
                while num + i in num_set:
                    streak += 1
                    i += 1
                longest_seq = max(streak, longest_seq)

        return longest_seq
