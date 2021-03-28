class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        out = []

        for i in range(len(nums) - 1):
            if i * 2 + 1 <= len(nums) - 1:
                freq = nums[i * 2]
                val = nums[i * 2 + 1]
                while freq:
                    out.append(val)
                    freq -= 1
            else:
                break

        return out