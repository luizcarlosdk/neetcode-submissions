class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort() # O(nlogn)

        for i, num in enumerate(nums):  # O(n)
            if i > 0 and num == nums[i-1]:
                continue

            target = -num
            l, r = i + 1, len(nums) - 1

            while l < r:  #O(n)
                current_sum = nums[l] + nums[r]
                if current_sum == target:
                    output.append([num,nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                elif current_sum < target:
                    l += 1
                else:
                    r -= 1
        
        return output
                    

        