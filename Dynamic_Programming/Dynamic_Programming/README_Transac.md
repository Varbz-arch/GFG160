# Stock Buy and Sell with Transaction Fee

You are given an array `arr[]` where `arr[i]` represents the price of a stock on the `i-th` day, and an integer `k` representing the transaction fee.

The task is to find the **maximum profit** you can achieve by completing as many transactions as you like, with the following constraints:

- You must pay the transaction fee `k` for each transaction.
- You cannot hold more than one stock at a time (sell before buying again).

---

## Approach

This problem is solved using **Dynamic Programming with two states**:

- `cash`: Maximum profit when **not holding** a stock
- `hold`: Maximum profit when **holding** a stock

### State Transitions

For each stock price:

- Sell the stock (if holding):
cash = max(cash, hold + price - k)


- Buy the stock (if not holding):
hold = max(hold, cash - price)

The transaction fee is applied during the **sell operation**.

---

## Example

### Input
```python
arr = [1, 3, 2, 8, 4, 9]
k = 2

The transaction fee is applied during the **sell operation**.

---

## Example

### Input
```python
arr = [1, 3, 2, 8, 4, 9]
k = 2

The transaction fee is applied during the **sell operation**.

---

## Example

### Input
```python
arr = [1, 3, 2, 8, 4, 9]
k = 2
O/P
8
Buy at 1 → Sell at 8 → Profit = 8 - 1 - 2 = 5
Buy at 4 → Sell at 9 → Profit = 9 - 4 - 2 = 3
Total Profit = 8