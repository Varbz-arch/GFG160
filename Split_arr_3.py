# Given an array, arr[], determine if arr can be split into three consecutive parts such that the sum of each part is equal. If possible, return any index pair(i, j) in an array such that 
# sum(arr[0..i]) = sum(arr[i+1..j]) = sum(arr[j+1..n-1]), otherwise return an array {-1,-1}.
# Note: Since multiple answers are possible, return any of them. The driver code will print true if it is correct otherwise, it will print false.
# Examples :
# Input:  arr[] = [1, 3, 4, 0, 4]
# Output: true
# Explanation: [1, 2] is valid pair as sum of subarray arr[0..1] is equal to sum of subarray arr[2..3] and also to sum of subarray arr[4..4]. The sum is 4, so driver code prints true.

#User function Template for python3
class Solution:
    
    def findSplit(self, arr):
        # Return an array of possible answer, driver code will judge and return true or false based on
        n = len(arr)
        total = sum(arr)
        if total % 3 != 0:
            return [-1, 1]
        target = total // 3
        prefix_sum = 0
        i = j = -1
        for idx in range(n):
            prefix_sum += arr[idx]
            if prefix_sum == target and i == -1:
                i = idx
            elif prefix_sum ==2 * target and i != -1:
                j = idx
                break
        if i != -1 and j != -1 and j<n-1:
            return [i, j]
        return [-1,1]
    
arr = [1, 2, 3, 0, 3]
sol = Solution()

result = sol.findSplit(arr)
print(result)