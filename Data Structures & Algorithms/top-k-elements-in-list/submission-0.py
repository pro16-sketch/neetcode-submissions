class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []

        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 1
            else:
                count[nums[i]] += 1

        lis = sorted(count.items(), key=lambda x: x[1])

        for i in range(1, k + 1):
            res.append(lis[-i][0])

        return res
        