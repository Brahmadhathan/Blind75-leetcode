class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n= len(nums)
        output= [1] *n # Initialize output list with 1s

        left = 1
        for i in range(n):
            output[i] *= left 
            left *= nums[i]
        right = 1
        for i in range(len(nums)-1,-1,-1):
            output[i] *= right
            right *= nums[i]
        
        return output
