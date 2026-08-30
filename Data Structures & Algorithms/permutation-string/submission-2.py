from collections import Counter
from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter=Counter(s1)
        window_size=len(s1)
        current_window=defaultdict(int)
        left=0
        for right in range(len(s2)):
            current_window[s2[right]]+=1
            if right-left+1>window_size:
                current_window[s2[left]]-=1
                if current_window[s2[left]]==0:
                    del current_window[s2[left]]
                left+=1
            if current_window==s1_counter:
                return True
        return False
        
        