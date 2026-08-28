class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        seen = set()
        max_length = 0

        while right < len(s):
            if s[right] not in seen:
                seen.add(s[right])
                max_length = max(max_length, right - left + 1)
                right += 1
            else:
                seen.remove(s[left])
                left += 1
        return max_length