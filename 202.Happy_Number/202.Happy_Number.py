class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        visited = []

        while(True):
            sum = 0
            string = str(n)
            for c in string:
                sum += int(c)*int(c)
            if(sum == 1):
                return True
            else:
                n = sum
                if(sum in visited):
                    return False
                else:
                    visited.append(sum)
