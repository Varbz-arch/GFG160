# Reverse A LINKED LISTS
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class Solution:
    def reverseList(self, head):
        curr = head
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
def buildLinkedList(values):
    """Helper function to create linked list from list of values"""
    if not values:
        return None
    head = Node(values[0])
    curr = head
    for val in values[1:]:
        curr.next = Node(val)
        curr = curr.next
    return head

def printLinkedList(head):
    """Helper function to print linked list"""
    curr = head
    while curr:
        print(curr.data, end=" ")
        curr = curr.next
    print()
n = int(input("Enter number of nodes: "))
arr = list(map(int, input("Enter elements: ").split()))

head = buildLinkedList(arr)

print("Original List:")
printLinkedList(head)
sol = Solution()
reversed_head = sol.reverseList(head)

print("Reversed List:")
printLinkedList(reversed_head)
