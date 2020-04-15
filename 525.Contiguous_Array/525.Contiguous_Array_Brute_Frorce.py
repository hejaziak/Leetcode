class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        group = []
        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                sub = []
                for k in range(i, j+1):
                    sub.append(nums[k])
                group.append(sub)

        maxLength = 0
        for x in group:
            if(isContiguous(x)):
                maxLength = max(maxLength, len(x))

        return maxLength


def isContiguous(arr):
    countZeros = 0
    countOnes = 0

    for a in arr:
        if(a == 0):
            countZeros += 1
        else:
            countOnes += 1

    if(countZeros == countOnes):
        return True
    else:
        return False
