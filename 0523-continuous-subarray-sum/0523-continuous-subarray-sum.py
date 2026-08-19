class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rem_map={0:-1}

        prefix=0

        for i in range(len(nums)):
            prefix+=nums[i]

            rem =prefix % k

            if rem in rem_map:
                if i-rem_map[rem]>=2:
                    return True
            else:
                rem_map[rem]=i
        return False