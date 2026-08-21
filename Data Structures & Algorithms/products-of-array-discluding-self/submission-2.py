#division method
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zerocnt = 0
        prod = 1
        arr = [0] * len(nums)

        for i in range(len(nums)):
            if nums[i] == 0:
                zerocnt += 1
            else:
                prod *= nums[i]

        if zerocnt > 1:
            return arr

        for i in range(len(nums)):
            if zerocnt == 1:
                if nums[i] == 0:
                    arr[i] = prod
                else:
                    arr[i] = 0
            else:
                arr[i] = prod // nums[i]

        return arr

        