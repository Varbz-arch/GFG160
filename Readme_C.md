
Explanation:
- Buy at 1, sell at 5 → profit = 4  
- Buy at 3, sell at 6 → profit = 3  
- Total = 7

---

## 💡 Approach
We use a **greedy algorithm**:
- Whenever today's price is greater than yesterday's, we take the difference as profit.
- The final answer is the sum of all such positive differences.

This works because buying at every local minimum and selling at every local maximum yields the maximum profit.

---

## ⏱️ Complexity
- **Time Complexity:** O(n)  
- **Space Complexity:** O(1)

---

## 🧑‍💻 Implementation
```python
from typing import List

class Solution:
    def maximumProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        for i in range(1, n):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit

# Example usage:
sol = Solution()
print(sol.maximumProfit([7,1,5,3,6,4]))  # Output: 7
print(sol.maximumProfit([1,2,3,4,5]))    # Output: 4
print(sol.maximumProfit([7,6,4,3,1]))    # Output: 0
