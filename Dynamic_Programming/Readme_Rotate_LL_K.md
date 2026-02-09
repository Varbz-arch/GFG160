Rotate Linked List (Python)
This program implements a solution to the Rotate Linked List problem.
It allows the user to input a linked list and a rotation count k, then rotates the linked list by k positions to the left.

Problem Statement
Given a singly linked list, rotate it by k positions.
Each rotation moves the head node to the end of the list.
The rotation is left rotation.
If k is greater than the length of the list, it rotates effectively by k % length.

Features
Takes user input for linked list values (space-separated).
Takes user input for k (number of rotations).
Builds a linked list from user input.
Performs rotation efficiently using modular arithmetic.
Prints the original and rotated linked list.

Example Input / Output
Input
Enter the linked list values (space separated): 10 20 30 40 50
Enter the value of k: 2
Output
Original Linked List:
10 -> 20 -> 30 -> 40 -> 50
Linked List after rotating by 2 positions:
30 -> 40 -> 50 -> 10 -> 20

Code Breakdown
1. Node Definition
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

Defines a linked list node with:
data → value of the node.
next → pointer to the next node.

2. Rotation Logic
class Solution:
    def rotate(self, head, k):
        ...
        return head

Steps:
Find the length of the linked list.
Adjust k using k % length to handle large values of k.
Make the list circular by connecting the last node to the head.
Move k steps forward from the head to find the new head.
Break the circular link to form the rotated list.

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
Reads integer k for number of rotations.

5. Running the Program
head = build_linked_list(values)
print("Original Linked List:")
print_linked_list(head)

solution = Solution()
new_head = solution.rotate(head, k)

print(f"Linked List after rotating by {k} positions:")
print_linked_list(new_head)

Builds the linked list.
Prints the original list.
Calls rotate() to rotate nodes.
Prints the rotated list.

Key Points
Time Complexity: O(n) (each node is visited once).
Space Complexity: O(1) (in-place rotation).
Works for any k ≥ 0.
Uses modulo operation to handle large k.