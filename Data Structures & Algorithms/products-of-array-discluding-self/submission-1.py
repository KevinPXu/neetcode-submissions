import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        beforeProd = 1
        for i in range(len(nums)):
            output[i] = beforeProd
            beforeProd *= nums[i]

        afterProd = 1
        for i in reversed(range(len(nums))):
            output [i] *= afterProd
            afterProd *= nums[i]

        return output       