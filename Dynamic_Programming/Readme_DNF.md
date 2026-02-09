# Dutch National Flag Problem (Sort 0s, 1s, and 2s)

This repository contains a Python implementation of the **Dutch National Flag algorithm**, also known as the **0-1-2 Sort problem**.  
It sorts an array consisting only of `0`, `1`, and `2` in a single pass with **O(n)** time complexity and **O(1)** extra space.

## Problem Statement
Given an array of size `n` containing only `0`, `1`, and `2`, sort the array in ascending order **without using any sorting algorithm like quicksort or mergesort**.

## Algorithm (Dutch National Flag)
- Use three pointers: `low`, `mid`, and `high`.
- Traverse the array:
  - If `arr[mid] == 0` → swap with `arr[low]`, increment both.
  - If `arr[mid] == 1` → just move `mid`.
  - If `arr[mid] == 2` → swap with `arr[high]`, decrement `high`.

This ensures all `0`s are on the left, all `1`s in the middle, and all `2`s on the right.

