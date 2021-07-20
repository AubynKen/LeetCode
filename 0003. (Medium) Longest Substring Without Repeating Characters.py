class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        start = 0
        max_length = 0
        for i, ch in enumerate(s):
            if ch in seen and seen[ch] >= start:
                start = seen[ch] + 1
            seen[ch] = i
            max_length = max(max_length, i - start + 1)
        return max_length
        