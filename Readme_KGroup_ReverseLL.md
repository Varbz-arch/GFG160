Reverse Nodes in k-Group (Python)
This program implements a solution to the "Reverse Nodes in k-Group" linked list problem.
It allows the user to input a linked list and a group size k, then reverses the nodes of the list in groups of size k. If the number of nodes remaining at the end is less than k, those nodes remain unchanged.

Problem Statement
Given a linked list, reverse the nodes of the list k at a time and return its modified list.
Nodes are reversed in groups of size k.
If the remaining number of nodes is less than k, leave them as is.

Features
Takes user input for linked list values (space-separated).
Takes user input for k (group size).
Builds a linked list from input values.
Reverses nodes in groups of k.
Prints the original and modified linked list.

Example Input / Output
Input
Enter the linked list values (space separated): 1 2 3 4 5 6 7 8
Enter the value of k: 3
Output
Original Linked List:
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
Linked List after reversing in groups of k:
3 -> 2 -> 1 -> 6 -> 5 -> 4 -> 7 -> 8

Code Breakdown
1. Node Definition
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

Defines a linked list node with a value (val) and a pointer to the next node.

2. Solution Class
class Solution:
    def reverseKGroup(self, head, k):
        ...
        return newHead

The main function that reverses nodes in groups of k.

Uses:
prev, curr, next pointers for reversing.
tail to keep track of the end of the last reversed group.
Handles leftover nodes (< k) by leaving them unchanged.

3. Helper Functions
def build_linked_list(values):
    ...
def print_linked_list(head):
    ...

build_linked_list(values): Converts user input list into a linked list.
print_linked_list(head): Prints the linked list in a -> b -> c format.

4. User Input Section
values = list(map(int, input("Enter the linked list values (space separated): ").split()))
k = int(input("Enter the value of k: "))

Takes space-separated integers as linked list values.
Reads integer k for group size.

5. Running the Program
head = build_linked_list(values)
print("Original Linked List:")
print_linked_list(head)

solution = Solution()
new_head = solution.reverseKGroup(head, k)

print("Linked List after reversing in groups of k:")
print_linked_list(new_head)

Builds the linked list.
Prints the original list.
Calls reverseKGroup() to reverse nodes in groups of k.
Prints the final modified list.

Key Points
Time Complexity: O(n) (each node is visited once).
Space Complexity: O(1) (in-place reversal, no extra storage).
Works for any k ≥ 1.