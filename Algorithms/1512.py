class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Output: 4   Input: nums = [1,2,3,1,1,3]

        count = 0
        N = len(nums)
        for i in range(N):
            for j in range(N):
                if nums[i] == nums[j] and i < j:
                    count += 1
        return count