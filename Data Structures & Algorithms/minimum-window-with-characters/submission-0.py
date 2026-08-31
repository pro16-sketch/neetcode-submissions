from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        required = Counter(t)
        window = Counter()

        left = 0
        right = 0

        have = 0
        need = len(required)

        min_length = float("inf")
        result = ""

        while right < len(s):
            ch = s[right]
            window[ch] += 1

            if ch in required and window[ch] == required[ch]:
                have += 1

            while have == need:
                window_length = right - left + 1

                if window_length < min_length:
                    min_length = window_length
                    result = s[left:right + 1]

                window[s[left]] -= 1

                if s[left] in required and window[s[left]] < required[s[left]]:
                    have -= 1

                left += 1

            right += 1

        return result