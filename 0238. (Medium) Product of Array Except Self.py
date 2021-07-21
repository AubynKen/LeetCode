class Solution:
    def productExceptSelf(self, nums):
        res = []  # the result
        # res[i] can be expressed as the product of all the numbers on the left, times all the numbers on the right
        # we multiply all the numbers on the left, traverse the array and append the left product to the res at each step
        p = 1  # product
        for x in nums:
            res.append(p)
            p *= x  # p is the product of nums[0:len(res) - 1]
        # we do the same thing from the right to the left
        p = 1
        for i in range(len(nums) - 1, -1):
            res[i] *= p
            p *= nums[i]  # p is the product of nums[i + 1:end]
        return res
