class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
            longest_sequence = 0
            num_set = set()
            for num in nums:
                num_set.add(num)
            
            for num in nums:
                # 1 2 3 4
                if num-1 not in num_set:
                    length = 1
                    while num + length in num_set:
                        length += 1
                    
                    longest_sequence = max(longest_sequence, length)

            return longest_sequence

