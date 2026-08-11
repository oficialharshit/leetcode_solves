class Solution(object):
    def missingInteger(self, arr):
        j = 0
        n = len(arr)
        for i in range(n-1):
            if arr[i+1] == arr[i] +1:
                j+=1
            else:
                break

        sm = sum(arr[:j+1])
    
        

        while sm in arr:
                sm+=1
        return sm
        