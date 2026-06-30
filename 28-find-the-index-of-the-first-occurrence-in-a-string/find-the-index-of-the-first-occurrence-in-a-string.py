class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        # Every possible starting index
        for i in range(len(haystack) - len(needle) + 1):

            # Assume it matches
            match = True

            # Compare every character
            for j in range(len(needle)):
                if haystack[i + j] != needle[j]:
                    match = False
                    break

            if match:
                return i

        return -1