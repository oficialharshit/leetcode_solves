class Solution(object):
    def majorityElement(self, arr):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count1 = 0
        count2 =0
        el2 = 0
        el1 = 0 
        for i in range(len(arr)):
            if arr[i] == el1:
                count1 += 1
            elif arr[i] == el2:
                count2 += 1
            elif count1 == 0:
                el1 = arr[i]
                count1 = 1
            elif count2 == 0:
                el2 = arr[i]
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
        count3=0
        count4=0
        ans =[]
        for i in range(len(arr)):
            if arr[i]==el1:
                count3+=1
            elif arr[i]==el2:
                count4+=1
            
        if count3 > len(arr) // 3:
            ans.append(el1)

        if count4 > len(arr) // 3:
            ans.append(el2)
        return ans
        