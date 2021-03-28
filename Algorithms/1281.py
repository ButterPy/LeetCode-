class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = str(n)
        mas = list(map(int, n))
        mult = 1

        for i in mas:
            mult *= i

        return mult - sum(mas)