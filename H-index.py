# You are given an array citations[], where each element citations[i] 
# represents the number of citations received by the ith paper of a researcher. 
# You have to calculate the researcher’s H-index.
# The H-index is defined as the maximum value H, 
# such that the researcher has published at least H papers, 
# and all those papers have citation value greater than or equal to H.
# Input: citations[] = [3, 0, 5, 3, 0]
# Output: 3
# Explanation: There are at least 3 papers with citation counts of 3, 5, and 3, 
# all having citations greater than or equal to 3.


class Solution:
    def hIndex(self, citations):
        citations.sort(reverse=True)   # Sort in descending order
        h = 0
        for i, c in enumerate(citations, 1):  # i starts at 1
            if c >= i:   # At least i papers with >= i citations
                h = i
        return h
    
# OR
# n= len(citations) 
# # freq=[0]*(n+1) # for citation in citations: 
# # if citation>=n: 
# # freq[n]+=1 
# # else: 
# # freq[citation]+=1 
# # index=n 
# # s=freq[n] 
# # while s< index: 
# # index-=1 
# # s+=freq[index] 
# # return index
if __name__ == "__main__":
    n = int(input("Enter number of papers: "))
    citations = list(map(int, input("Enter citation counts separated by space: ").split()))

    obj = Solution()
    result = obj.hIndex(citations)
    print("H-index:", result)