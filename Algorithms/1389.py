class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        from collections import deque
        arr = deque()

        for id, i in enumerate(index):
            arr.insert(i, nums[id])
        return arr