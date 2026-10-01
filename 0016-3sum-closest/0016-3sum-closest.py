class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()

        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):

            j = i + 1
            k = len(nums) - 1

            while j < k:

                currsum = nums[i] + nums[j] + nums[k]

                # Exact answer
                if currsum == target:
                    return currsum

                # Update closest sum
                if abs(currsum - target) < abs(closest - target):
                    closest = currsum

                # Move pointers
                if currsum < target:
                    j += 1
                else:
                    k -= 1

        return closest