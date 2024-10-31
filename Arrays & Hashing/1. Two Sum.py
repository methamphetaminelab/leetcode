class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for num in range(len(nums)):
            for num2 in range(num):
                if nums[num] + nums[num2] == target:
                    return [num, num2]