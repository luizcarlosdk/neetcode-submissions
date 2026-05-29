class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        val_to_idx = {}

        for i in range(len(nums)):
            complement = target- nums[i]

            if complement in val_to_idx:
                return [val_to_idx[complement], i]
            
            val_to_idx[nums[i]] = i
        