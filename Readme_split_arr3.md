# Split Array into Three Equal Sum Parts

This program checks whether a given array can be split into **three consecutive parts** such that the **sum of each part is equal**.

If possible, it returns **any valid pair of indices (i, j)** where:
- `sum(arr[0..i]) = sum(arr[i+1..j]) = sum(arr[j+1..n-1])`

If not possible, it returns:
[-1, -1]


---

## Approach

1. Calculate the total sum of the array.
2. If the total sum is not divisible by 3, splitting is impossible.
3. Traverse the array using a prefix sum:
   - Find the first index `i` where prefix sum equals `total/3`
   - Find the first index `j` where prefix sum equals `2*(total/3)`
4. Return the indices `(i, j)`.

---

## Example

**Input**
```python
arr = [1, 2, 3, 0, 3]

output
[1, 3]

explanation
[1, 2] | [3, 0] | [3]
Each part has sum = 3.