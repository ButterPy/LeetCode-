class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        # Output: "1[.]1[.]1[.]1"    Input: address = "1.1.1.1"

        addressNew = address.replace(".", "[.]")
        return addressNew