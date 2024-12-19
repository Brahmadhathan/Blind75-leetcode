class Solution:
    def twoSum(self,num:list [int],target :int) -> list[int]:
        for i in range(len(num)):
            for j in range(i+1 , len(num)):
                if num[j] == target - num[i]:
                    return [i,j]
        return[]