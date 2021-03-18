class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # Output: [1,3,6,10]    Input: nums = [1,2,3,4]

        temp = 0
        numsCopy = []

        for i in range(len(nums)):
            numsCopy.append(temp + nums[i])
            temp += nums[i]
        return numsCopy