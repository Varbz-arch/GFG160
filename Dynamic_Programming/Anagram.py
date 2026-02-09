# Given two non-empty strings s1 and s2, 
# consisting only of lowercase English letters,
#  determine whether they are anagrams of each other or not.
# Two strings are considered anagrams if they contain 
# the same characters with exactly the same frequencies, regardless of their order.

# Input: s1 = "geeks" s2 = "kseeg"
# Output: true
class Solution:
    def areAnagrams(self, s1, s2):
       # code here
       return sorted(s1)==sorted(s2)
   
if __name__ == "__main__":
    s1 = input("Enter first string: ").strip()
    s2 = input("Enter second string: ").strip()

    sol = Solution()
    if sol.areAnagrams(s1, s2):
        print("Yes, the strings are anagrams.")
    else:
        print("No, the strings are not anagrams.")