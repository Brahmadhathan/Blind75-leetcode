class Solution:
    def maxProfit(self, price: list[int]) -> int:
        curmax=0
        globalmax=0 
        for i in range(1,len(price)):
            curmax = max(curmax + (price[i]-price[i-1]),0)
            globalmax = max(globalmax,curmax)
        return globalmax

        