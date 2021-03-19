class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        out = [0] * 101

        for i in nums:
            out[i] += 1

        count = 0

        for i in range(len(out)):
            temp = out[i]
            out[i] = count
            count += temp

        return [out[i] for i in nums]