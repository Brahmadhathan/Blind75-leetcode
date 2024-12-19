class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp=[[0 for i in range(len(text2)+ 1)]for j in range(len(text1)+ 1)]
        #the above code is getting the 2D of length text2+1 and text1+1 and initilizing it to 0
        for i in range(len(text1) - 1,-1,-1): #to get in reverse order
            for j in range(len(text2) - 1,-1,-1):
                if text1[i] == text2[j]:
                    dp[i][j]= 1 + dp[i+1][j+1]
                else:
                    dp[i][j]= max(dp[i][j+1],dp[i+1][j])
        return dp[0][0]

