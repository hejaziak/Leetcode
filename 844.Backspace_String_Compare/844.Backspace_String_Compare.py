class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """

        stackS = []
        stackT = []

        for char in S:
            if(char != '#'):
                stackS.append(char)
            elif (len(stackS) > 0):
                stackS.pop()

        for char in T:
            if(char != '#'):
                stackT.append(char)
            elif (len(stackT) > 0):
                stackT.pop()

        if(stackT == stackS):
            return True
        else:
            return False
