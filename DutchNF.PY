# Given an array arr[] containing only 0s, 1s, and 2s. Sort the array in ascending order.
# Note: You need to solve this problem without utilizing the built-in sort function.
# using DUTCH NATIONAL FLAG ALGO
# Input: arr[] = [0, 1, 2, 0, 1, 2]
# Output: [0, 0, 1, 1, 2, 2]
# Explanation: 0s, 1s and 2s are segregated into ascending order.

class Solution:
    def sort012(self, arr):
        # code here
        n=len(arr)
        low=0
        high=n-1
        mid=0
        while (mid<=high):
            if arr[mid]==0:
                arr[low], arr[mid]=arr[mid], arr[low]
                low=low+1
                mid=mid+1
            elif arr[mid]==1:
                mid=mid+1
            else:
                arr[mid], arr[high]=arr[high], arr[mid]
                high=high-1
        return arr
if __name__ == "__main__":
    n = int(input("Enter number of elements: "))
    arr = list(map(int, input("Enter elements (0,1,2 only): ").split()))
    
    obj = Solution()
    sorted_arr = obj.sort012(arr)
    
    print("Sorted array:", *sorted_arr)