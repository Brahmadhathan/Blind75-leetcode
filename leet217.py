class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums.sort() #sort the array in the assending order

        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False
        