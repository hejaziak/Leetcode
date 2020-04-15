class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product = 1
        left = [1]*len(nums)
        right = [1]*len(nums)

        # left
        for i in range(1, len(nums)):
            left[i] = left[i-1]*nums[i-1]
        # right
        for i in reversed(range(len(nums)-1)):
            right[i] = nums[i+1] * right[i+1]

        result = []
        for i in range(len(nums)):
            result.append(left[i]*right[i])

        return result
