# Anagram Checker

## Problem Statement
Given two non-empty strings `s1` and `s2`, consisting only of lowercase English letters,  
determine whether they are **anagrams** of each other.

Two strings are anagrams if:
- They contain the **same characters**,
- With the **same frequency**,
- Regardless of order.

## Examples
Input:
s1 = "listen"
s2 = "silent"
Output:
Yes, they are anagrams.
Input:
s1 = "hello"
s2 = "world"
Output:
No, they are not anagrams.
## Approach
We use Python’s `collections.Counter`:
- Count the frequency of characters in both strings.
- Compare the frequency maps.
- If they are equal → the strings are anagrams.
##  Complexity
- **Time Complexity:** O(n)  
- **Space Complexity:** O(1) (since only 26 lowercase letters exist)

