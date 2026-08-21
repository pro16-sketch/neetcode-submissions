class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #what should i write now??????
        s1=sorted(s)
        t1=sorted(t)
        if s1==t1:
                return True
        return False
