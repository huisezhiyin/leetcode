class Solution:
    def minNumberInRotateArray(self, rotateArray):
        length = len(rotateArray)
        if length == 0:
            return rotateArray
        low = 0
        high = length - 1
        if rotateArray[low] < rotateArray[high]:
            return rotateArray[low]
        else:
            while (high - low) > 1:
                mid = (low + high) / 2
                if rotateArray[low] <= rotateArray[mid]:
                    low = mid
                elif rotateArray[mid] <= rotateArray[high]:
                    high = mid
                elif rotateArray[low] == rotateArray[high] == rotateArray[mid]:
                    for i in range(length):
                        if rotateArray[i] < rotateArray[0]:
                            high = i
            result = rotateArray[high]
            return result
