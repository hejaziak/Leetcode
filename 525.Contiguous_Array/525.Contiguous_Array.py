class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mem = {0: 0}  # stores {count:first index of that count}
        count = 0
        length = 0
        for (i, x) in enumerate(nums):
            count += 2*x-1
            if(count in mem):
                length = max(length, i - mem[count] + 1)

            else:
                mem[count] = i + 1

        return length
