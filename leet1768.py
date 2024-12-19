class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        #zip function can be used to get multiple data at a time
        for a,b in zip(word1,word2):
            merged.append(a+b) #merging the words in a and b
        
        merged.append(word1[len(word2):])
        merged.append(word2[len(word1):])
        return "".join(merged)
