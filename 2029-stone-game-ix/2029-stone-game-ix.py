class Solution(object):
    def stoneGameIX(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        count = [0, 0, 0]

        for stone in stones:
            count[stone % 3] += 1

        zero,one,two = count

        # Even number of remainder-0 stones 
        if zero % 2 == 0:
            return one > 0 and two > 0

        # Odd number of remainder-0 stones
        return abs(one - two) > 2