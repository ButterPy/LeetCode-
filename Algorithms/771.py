class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        # Output: 3     Input: jewels = "aA", stones = "aAAbbbb"

        count = 0
        for i in stones:
            if i in jewels:
                count += 1
        return count