class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        # Output  [2,3,5,4,1,7]     Input: nums = [2,5,1,3,4,7], n = 3

        mas = []
        N = len(nums)

        for index in range(N // 2):
            mas.append(nums[index])
            mas.append(nums[index + N // 2])

        return mas
