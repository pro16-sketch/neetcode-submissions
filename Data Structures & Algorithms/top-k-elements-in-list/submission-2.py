class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm={}
        arr=[]
        for i in nums:
            hm[i]=hm.get(i,0)+1
        freq=[[] for i in range(len(nums)+1)]
        for nums,count in hm.items():
            freq[count].append(nums)
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                arr.append(num)
                if len(arr)==k:
                    return arr