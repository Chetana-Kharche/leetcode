class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        freq = {0: -1}
        
        prefix = 0
        maxlen = 0

        for i in range(len(nums)):

            # Treat 0 as -1 and 1 as +1
            if nums[i] == 0:
                prefix -= 1
            else:
                prefix += 1

            # Same prefix sum means equal 0s and 1s
            if prefix in freq:
                currlen = i - freq[prefix]
                maxlen = max(maxlen, currlen)
            else:
                # Store first occurrence only
                freq[prefix] = i

        return maxlen