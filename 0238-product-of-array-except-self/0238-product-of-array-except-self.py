class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        sufix = [0] * n
        prefix = [0] * n

        prefix[n - 1] = 1
        sufix[0] = 1

        # Product of elements to the RIGHT
        for i in range(n - 2, -1, -1):
            prefix[i] = prefix[i + 1] * nums[i + 1]

        # Product of elements to the LEFT
        for i in range(1, n):
            sufix[i] = sufix[i - 1] * nums[i - 1]

        # Left product × Right product
        for i in range(n):
            nums[i] = prefix[i] * sufix[i]

        return nums