import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        idx = 0
        while idx < len(nums):
            ans.append(math.prod(nums[:idx]) * math.prod(nums[idx + 1:]))
            idx += 1
        return ans       