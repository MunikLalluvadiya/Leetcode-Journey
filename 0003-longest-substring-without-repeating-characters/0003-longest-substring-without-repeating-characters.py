class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        left = 0
        max_len = 0
        window = ""  # keeps track of current substring without repeats

        for right in range(len(s)):
            char = s[right]

            # If char is already in our window, shrink from the left
            while char in window:
                window = window[1:]   # remove the first character
                left += 1

            window += char  # add current character to window
            max_len = max(max_len, len(window))

        return max_len