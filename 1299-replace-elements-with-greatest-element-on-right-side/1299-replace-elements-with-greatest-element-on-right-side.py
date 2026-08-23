class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        nums = arr[:]
        maxim = -1
        for i in range(len(nums)-1,0,-1):
            nums[i] = maxim
            if arr[i]>maxim:
                maxim = arr[i]
        nums[0] = maxim
        return nums