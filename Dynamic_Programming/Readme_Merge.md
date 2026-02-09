# Merge Two Sorted Linked Lists (Python)
This project demonstrates how to merge two **sorted singly linked lists** into one sorted list.  
It uses an iterative approach with a dummy node for simplicity.
## Problem Statement
Given the heads of two sorted linked lists, merge them into a single sorted linked list.
Example:
Input:
List 1: 1 → 3 → 5
List 2: 2 → 4 → 6
Output:
1 → 2 → 3 → 4 → 5 → 6
## Code Structure
- `Node` : Represents a node in the linked list with `data` and `next`.
- `Solution.sortedMerge(head1, head2)` : Merges two sorted linked lists into one sorted list.
- `buildLinkedList(values)` : Helper function to create a linked list from a Python list.
- `printLinkedList(head)` : Helper function to print the linked list.