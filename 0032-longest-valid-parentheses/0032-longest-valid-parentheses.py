class Solution:
    def longestValidParentheses(self, s):
        stack = [-1]
        maxlen = 0

        for i in range(len(s)):

            if s[i] == '(':
                stack.append(i)

            else:
                stack.pop()

                if not stack:
                    stack.append(i)
                else:
                    currlen = i - stack[-1]
                    maxlen = max(maxlen, currlen)

        return maxlen
        