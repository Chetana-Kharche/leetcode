class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = {}
        window = {}
        result = []

        for c in p:
            need[c] = need.get(c, 0) + 1

        i = 0

        for j in range(len(s)):
            window[s[j]] = window.get(s[j], 0) + 1

            # Keep window size equal to len(p)
            if j - i + 1 > len(p):
                window[s[i]] -= 1

                if window[s[i]] == 0:
                    del window[s[i]]

                i += 1

            # Check anagram
            if j - i + 1 == len(p):
                if window == need:
                    result.append(i)

        return result