class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        mapping = {}
        
        for num_index in range(0, len(nums)):
            second_number = target - nums[num_index]
            if second_number in mapping and num_index!=nums.index(second_number):
                 
                result.append(num_index)
                result.append(nums.index(second_number))
            
            mapping[nums[num_index]] = num_index
        
        return result
        