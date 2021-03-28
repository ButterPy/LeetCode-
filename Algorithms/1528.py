class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """

        mas = [0] * len(s)

        for id, i in enumerate(indices):
            mas[i] = s[id]

        return "".join(mas)