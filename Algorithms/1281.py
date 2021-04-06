class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        from functools import reduce
        arr = []

        while n:
            arr.append(n % 10)
            n //= 10
        out = reduce(lambda x, y: x * y, arr) - sum(arr)
        return out
