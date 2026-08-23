class Solution(object):
    def replaceElements(self, arr):
        nums = arr[:]
        maxim = -1

        for i in range(len(nums)-1, -1, -1):
            nums[i] = maxim
            if arr[i] > maxim:
                maxim = arr[i]

        return nums

        
