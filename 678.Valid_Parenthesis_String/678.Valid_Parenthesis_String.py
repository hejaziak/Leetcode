class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        jokers = []

        for i, x in enumerate(s):
            if(x == "("):
                stack.append((i, x))
            if(x == ")"):
                if(len(stack) > 0):
                    stack.pop()
                elif(len(jokers) > 0):
                    jokers.pop()
                else:
                    return False
            if(x == "*"):
                jokers.append((i, x))

        if(len(stack) > len(jokers)):
            return False

        for i in reversed(range(len(stack))):
            index, x = stack.pop()
            jndex, y = jokers.pop()
            if(index > jndex):
                return False

        return True
