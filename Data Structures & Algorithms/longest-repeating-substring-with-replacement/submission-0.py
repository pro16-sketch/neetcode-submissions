class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        count = {}
        max_length = 0

        while right < len(s):
            ch = s[right]

            if ch not in count:
                count[ch] = 1
            else:
                count[ch] += 1

            max_char = max(count.values())

            windowLength = right - left + 1
            replacements = windowLength - max_char

            if replacements > k:
                count[s[left]] -= 1
                left += 1
            else:
                max_length = max(max_length, windowLength)

            right += 1

        return max_length