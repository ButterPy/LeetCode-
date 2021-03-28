class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        key = {
            'type':  0,
            'color': 1,
            'name':  2
        }

        count = 0

        for i in items:
            if i[key[ruleKey]] == ruleValue:
                count += 1
        return count
