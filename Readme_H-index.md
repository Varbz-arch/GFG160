# H-Index Problem
This repository contains a Python solution for the **H-index problem**, a popular interview and LeetCode/GFG question.

## 📌 Problem Statement
The **H-index** is defined as the maximum value `h` such that the given researcher has published at least `h` papers that have each been cited at least `h` times.

Given an array `citations` where `citations[i]` is the number of citations for the `i-th` paper, return the researcher's H-index.
Input:
Enter number of papers: 5
Enter citation counts separated by space: 3 0 6 1 5
Output:
H-index: 3

Explanation:
- Papers sorted by citations: `[6, 5, 3, 1, 0]`  
- At least 3 papers have **3 or more** citations → H-index = 3
## ⚙️ Algorithm
1. Sort the array in descending order.
2. Traverse the array and find the largest `i` such that `citations[i] >= i+1`.
3. Return that value as the H-index.
## 💻 Code

class Solution:
    def hIndex(self, citations):
        citations.sort(reverse=True)
        for i, c in enumerate(citations, 1):
            if c < i:
                return i - 1
        return len(citations)


if __name__ == "__main__":
    n = int(input("Enter number of papers: "))
    citations = list(map(int, input("Enter citation counts separated by space: ").split()))

    obj = Solution()
    result = obj.hIndex(citations)
    print("H-index:", result)

