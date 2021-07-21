class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, number in enumerate(nums):
            if number in seen:
                return [seen[number], i]
            seen[target - number] = i