class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        complemMap = {} # val: index

        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in complemMap:
                return [complemMap[difference], i]
            
            complemMap[nums[i]] = i
        
        return []
        