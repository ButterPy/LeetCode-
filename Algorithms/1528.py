class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        d = dict()
        count = 0
        out = []

        for i in indices:
            d[i] = s[count]
            count += 1

        indices.sort()

        for i in indices:
            out.append(d.get(i))
        return ''.join(out)