class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start=0
        end=len(numbers)-1
        while start!=end:
            Sum= numbers[start]+numbers[end]
            if Sum==target:
                return [start+1, end+1]
            elif Sum<target:
                start+=1
            else:
                end-=1