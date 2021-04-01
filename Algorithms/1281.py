class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        from functools import reduce

        arr = list(map(int, str(n)))
        mult = reduce(lambda a, b: a + b, arr)
        result = reduce(lambda a, b: a * b, arr) - mult

        return result