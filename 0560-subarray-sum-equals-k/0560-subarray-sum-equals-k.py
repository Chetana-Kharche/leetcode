class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        count=0
        prefixSum=[0]*n

        prefixSum[0]=nums[0]

        for i in range(1, n):
            prefixSum[i] = prefixSum[i - 1] + nums[i]
        
        freq={}

        for j in range(n):
            # Case 1: prefix sum itself is k
            if prefixSum[j] == k:
                count += 1

            # Case 2: find prefixSum[j] - k
            val = prefixSum[j] - k

            if val in freq:
                count += freq[val]

            # Store current prefix sum
            if prefixSum[j] not in freq:
                freq[prefixSum[j]] = 0

            freq[prefixSum[j]] += 1

        return count

