class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        
        max_length = 0
        
        for num in nums:
            if num - 1 not in nums:
                current_num = num
                current_streak = 1
                
                while current_num + 1 in nums:
                    current_num += 1
                    current_streak += 1
                
                max_length = max(max_length, current_streak)

        return max_length