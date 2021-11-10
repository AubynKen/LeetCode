class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        curr = numbers[0] + numbers[-1]
        while curr != target:
            if curr < target:
                i += 1
                curr = numbers[i] + numbers[j]
            else:
                j -= 1
                curr = numbers[i] + numbers[j]
        return [i + 1, j + 1]
    