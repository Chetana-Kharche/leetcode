class Solution:
    def findSubstring(self, s, words):
        result = []

        if not words or not words[0]:
            return result

        word_len = len(words[0])
        word_count = {}

        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

        for start in range(word_len):
            left = start
            right = start
            window = {}
            count = 0

            while right + word_len <= len(s):
                word = s[right:right + word_len]
                right += word_len

                if word in word_count:
                    window[word] = window.get(word, 0) + 1
                    count += 1

                    while window[word] > word_count[word]:
                        left_word = s[left:left + word_len]
                        window[left_word] -= 1
                        left += word_len
                        count -= 1

                    if count == len(words):
                        result.append(left)

                else:
                    window = {}
                    count = 0
                    left = right

        return result