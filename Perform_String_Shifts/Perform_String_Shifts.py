class Solution(object):
    def stringShift(self, s, shift):
        """
        :type s: str
        :type shift: List[List[int]]
        :rtype: str
        """

        leftSum = 0
        rightSum = 0
        for op in shift:
            if(op[0] == 0):
                leftSum += op[1]
            else:
                rightSum += op[1]

        total = leftSum - rightSum

        if(total > 0):
            for i in range(abs(total)):
                s = rotateLeft(s)
                print(s)
        else:
            for i in range(abs(total)):
                s = rotateRight(s)

        return s


def rotateLeft(s):
    """
    :type arr: int[]
    :rtyp: int[]
    """
    element = s[0]
    s = s[1:len(s)] + element
    return s


def rotateRight(s):
    """
    :type arr: int[]
    :rtyp: int[]
    """
    element = s[len(s)-1]
    s = element + s[0:len(s)-1]
    return s
