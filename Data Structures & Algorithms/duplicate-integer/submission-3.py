class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         num_set = set(nums)
         print(num_set)
         if len(num_set) == len(nums): 
            return False
         return True
