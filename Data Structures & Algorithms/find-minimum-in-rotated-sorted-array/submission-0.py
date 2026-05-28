class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        output = nums[0]

        while l <= r:
            middle = (l+r)//2
            output = min(output, nums[middle])

            if nums[middle] > nums[-1]:
                l = middle + 1
            else:
                r = middle - 1
        
        return output
