class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix = [1] * len(nums)
        prod = 1

        for i in range(len(nums)):
            prefix[i] = prod
            prod *= nums[i]


        suffix = [1] * len(nums)
        prod = 1

        for i in range(len(nums) - 1, -1, -1):
            suffix[i] = prod
            prod *= nums[i]

        result = [0] * len(nums)

        for i in range(len(nums)):
            result[i] = prefix[i] * suffix[i]

        return result