# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.
# Interleaving of two strings s1 and s2 is a way to mix their characters to form a new string s3, 
# while maintaining the relative order of characters from s1 and s2. Conditions for interleaving:

# Characters from s1 must appear in the same order in s3 as they are in s1.
# Characters from s2 must appear in the same order in s3 as they are in s2.
# The length of s3 must be equal to the combined length of s1 and s2.

# Input: s1 = "AAB", s2 = "AAC", s3 = "AAAABC"
# Output: true
# Explanation: The string "AAAABC" has all characters of the other two strings and in the same order.


class Solution:
    def isInterleave(self, s1, s2, s3):
        # code here
        if len(s3) != len(s2)+len(s1):
            return False
        m,n = len(s1), len(s2)
        dp = [[False]* (n+1) for _ in range(m+1)]
        dp[0][0] = True
        for i in range(1, m+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for j in range(1, n+1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        for i in range(1, m+1):
            for j in range(1, n+1):
                dp[i][j] = (
                    (dp[i-1][j] and s1[i-1]== s3[i+j-1]) or
                    (dp[i][j-1] and s2[j-1]== s3[i+j-1])
                )
        return dp[m][n]
s1 = input("Enter string s1: ")
s2 = input("Enter string s2: ")
s3 = input("Enter string s3: ")

solution = Solution()
result = solution.isInterleave(s1, s2, s3)

if result:
    print("Yes, s3 is an interleaving of s1 and s2")
else:
    print("No, s3 is NOT an interleaving of s1 and s2")