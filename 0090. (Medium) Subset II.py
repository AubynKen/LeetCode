from collections import Counter

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        counts = Counter(nums)
        res = [[]]
        for num in counts.keys():
            new_res = []
            for i in range(counts[num] + 1):
                for sol in res:
                    new_res.append(sol + [num] * i)
            res = new_res
        return res
            