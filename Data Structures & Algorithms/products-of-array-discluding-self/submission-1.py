class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        prefix_array = []
        # nums = [1 2 4 6]
        # prefix = [1, 1, 2, 8]
        #build the prefix array
        for num in nums:
            prefix_array.append(prefix)
            prefix = prefix*num
        
        posfix = 1
        # multiple by nums in reverse
        for i in range(len(nums)-1, -1, -1):
            prefix_array[i] *= posfix
            posfix *= nums[i]
        
        return prefix_array





