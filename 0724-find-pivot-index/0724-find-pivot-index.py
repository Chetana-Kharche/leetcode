class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)

        prefix = [0] * n
        suffix = [0] * n

        # prefix[i] = sum of elements before i
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i - 1]

        # suffix[i] = sum of elements after i
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] + nums[i + 1]

        # Compare left and right sums
        for i in range(n):
            if prefix[i] == suffix[i]:
                return i

        return -1