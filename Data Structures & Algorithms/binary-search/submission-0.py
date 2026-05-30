class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for index, value in enumerate(nums):
            if target == value:
                return index
        else:
            return -1
        