class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        d = dict()

        for i in jewels:
            d[i] = 0

        for i in stones:
            if d.get(i) is not None:
                d[i] += 1
        return sum(d.values())