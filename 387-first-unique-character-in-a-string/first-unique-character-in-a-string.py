class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_count = {}
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        for index in range(len(s)):
            if char_count[s[index]] == 1:
                return index
        return -1
