class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        current_sum = sum(nums)
        
        expected_sum = ((len(nums)+1)*(len(nums)))//2
        
        return expected_sum - current_sum
        