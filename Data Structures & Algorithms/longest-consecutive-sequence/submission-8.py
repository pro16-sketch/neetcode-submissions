class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        numSet=set(nums)
        for num in numSet:
            if num-1 not in numSet:
                current=num 
                count=1
                while current+1 in numSet:
                    current+=1
                    count+=1
                longest=max(longest,count)
        return longest
                
                
        