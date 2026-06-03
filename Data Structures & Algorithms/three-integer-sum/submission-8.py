class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = set()
        nums.sort()
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                curr_sum = nums[l] + nums[r]
                if curr_sum == -nums[i]:
                    output.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif curr_sum < -1 * (nums[i]):
                    l += 1
                else:
                    r -= 1

        return [list(triplet) for triplet in output]
