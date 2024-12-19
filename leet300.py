class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        lis = [1]*len(nums) #caching
        for i in range(len(nums) - 1,-1,-1): #starting from the last index
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]: #cheching if 2<4 or the provided output
                    lis[i] = max(lis[i],1+lis[j])
        return max(lis)
        