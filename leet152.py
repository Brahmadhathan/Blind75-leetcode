class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        N = len(nums)

        _max= cur_max = cur_min = nums[0]

        for n in nums[1:] :
            temp = cur_max
            cur_max = max(cur_max*n,cur_min*n,n)
            cur_min = min(temp*n,cur_min*n,n)
            _max = max(_max,cur_max)
        return _max
        