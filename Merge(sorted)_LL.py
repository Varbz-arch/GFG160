# Given the head of two sorted linked lists consisting of nodes respectively.
#  Merge both lists and return the head of the sorted merged list.

class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None

class Solution:
    def sortedMerge(self, head1, head2):
        # code here
        dummy= Node(-1)
        curr=dummy
        while head1 and head2:
            if head1.data<=head2.data:
                curr.next=head1
                head1=head1.next
            else:
                curr.next=head2
                head2=head2.next
            curr=curr.next
        if head1:
            curr.next=head1
        if head2:
            curr.next=head2
        return dummy.next
        
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
n1 = int(input("Enter number of nodes in list 1: "))
arr1 = list(map(int, input("Enter elements of list 1 (sorted): ").split()))

n2 = int(input("Enter number of nodes in list 2: "))
arr2 = list(map(int, input("Enter elements of list 2 (sorted): ").split()))

head1 = buildLinkedList(arr1)
head2 = buildLinkedList(arr2)

print("List 1:")
printLinkedList(head1)
print("List 2:")
printLinkedList(head2)

sol = Solution()
merged_head = sol.sortedMerge(head1, head2)

print("Merged Sorted List:")
printLinkedList(merged_head)