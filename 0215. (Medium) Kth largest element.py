class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        pivot = random.choice(nums)
        small, large = [], []

        # partition into small large and pivot
        for x in nums:
            if x < pivot:
                small.append(x)
            elif x > pivot:
                large.append(x)
        pivot_count = len(nums) - len(small) - len(large)

        if k <= len(large):
            return self.findKthLargest(large, k)
        elif k > len(large) + pivot_count:
            return self.findKthLargest(small, k - len(large) - pivot_count)
        return pivot
