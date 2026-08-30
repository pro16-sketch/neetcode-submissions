class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        count = {}
        window = {}

        for ch in s1:
            if ch not in count:
                count[ch] = 1
            else:
                count[ch] += 1

        left = 0
        right = len(s1) - 1
        if len(s1) > len(s2):
            return False

        for i in range(left, right + 1):
            if s2[i] not in window:
                window[s2[i]] = 1
            else:
                window[s2[i]] += 1

        while right < len(s2):

            if count == window:
                return True

            window[s2[left]] -= 1

            if window[s2[left]] == 0:
                del window[s2[left]]

            left += 1
            right += 1

            if right < len(s2):
                if s2[right] not in window:
                    window[s2[right]] = 1
                else:
                    window[s2[right]] += 1

        return False
        