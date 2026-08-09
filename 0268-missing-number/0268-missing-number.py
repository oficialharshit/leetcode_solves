class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        xor1 = 0
        xor2 = 0

        for i in range(n):
            xor2 ^= nums[i]
            xor1 ^= i + 1

        

        return xor1 ^ xor2