class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        print(stones)
        while(len(stones) > 1):
            firstMax = max(stones)
            stones.remove(firstMax)
            secondMax = max(stones)
            stones.remove(secondMax)
            merged = abs(secondMax-firstMax)
            if(merged != 0):
                stones.append(merged)

        result = 0
        if(len(stones) > 0):
            result = stones[0]

        return result
