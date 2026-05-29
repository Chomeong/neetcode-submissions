class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for indexa, i in enumerate(nums):
            for indexb, j in enumerate(nums):
                if i+j == target and indexa != indexb:
                    return [indexa, indexb]
