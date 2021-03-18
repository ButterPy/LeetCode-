class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        # Output: 6   Input: accounts = [[1,2,3],[3,2,1]]

        accountsMax = []
        for i in accounts:
            accountsMax.append(sum(i))
        return max(accountsMax)
