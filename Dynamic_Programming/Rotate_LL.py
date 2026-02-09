# You are given the head of a singly linked list, 
# you have to left rotate the linked list k times. 
# Return the head of the modified linked list.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def rotate(self, head, k):
        if k == 0 or head is None:
            return head
        len = 1
        curr = head
        while curr.next is not None:
            len += 1
            curr = curr.next
        k = k % len
        if k == 0:
            return head
        curr.next = head
        curr = head
        for i in range(1, k):
            curr = curr.next
        head = curr.next
        curr.next = None

        return head


# -------- Helper functions --------
def build_linked_list(values):
    if not values:
        return None
    head = Node(values[0])
    curr = head
    for val in values[1:]:
        curr.next = Node(val)
        curr = curr.next
    return head

def print_linked_list(head):
    while head:
        print(head.data, end=" -> " if head.next else "\n")
        head = head.next


# -------- User Input Section --------
values = list(map(int, input("Enter the linked list values (space separated): ").split()))
k = int(input("Enter the value of k: "))

head = build_linked_list(values)
print("Original Linked List:")
print_linked_list(head)

solution = Solution()
new_head = solution.rotate(head, k)

print(f"Linked List after rotating by {k} positions:")
print_linked_list(new_head)
