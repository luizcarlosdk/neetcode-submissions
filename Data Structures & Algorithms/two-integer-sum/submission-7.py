class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_to_idx = {}

        for i in range(len(nums)):
            diff = target - nums[i] 
            if diff in val_to_idx:
                return [val_to_idx[diff], i]
            val_to_idx[nums[i]] = i
        
        return 


# returnm indices in any order?
# what if not found?
