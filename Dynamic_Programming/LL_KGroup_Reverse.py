# You are given the head of a Singly linked list. 
# You have to reverse every k node in the linked list 
# and return the head of the modified list.
# Note: If the number of nodes is not a multiple of k then 
# the left-out nodes at the end, should be considered as a group and must be reversed.

# Input: k = 2,
# head= 1-> 2-> 3-> 4-> 5-> 6
#    Output: 2 -> 1 -> 4 -> 3 -> 6 -> 5
# Explanation: Linked List is reversed in a group of size k = 2.
   
class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        curr = head
        newHead = None
        tail = None

        while curr:
            groupHead = curr
            count = 0
            prev = None

            temp = curr
            node_count = 0
            while temp and node_count < k:
                temp = temp.next
                node_count += 1
            
            if node_count < k:
                if tail:
                    tail.next = curr
                break

            while curr and count < k:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                count += 1

            if newHead is None:
                newHead = prev

            if tail is not None:
                tail.next = prev

            tail = groupHead

        return newHead
def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def print_linked_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "\n")
        head = head.next
values = list(map(int, input("Enter the linked list values (space separated): ").split()))
k = int(input("Enter the value of k: "))

head = build_linked_list(values)
print("Original Linked List:")
print_linked_list(head)

solution = Solution()
new_head = solution.reverseKGroup(head, k)

print("Linked List after reversing in groups of k:")
print_linked_list(new_head)
