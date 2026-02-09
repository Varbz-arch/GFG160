# Approach:
# Define two arrays prev and curr of size sum+1 to store the just previous row result 
# and current row result respectively.
# Once curr array is calculated then curr becomes our prev for the next row.
# When all rows are processed the answer is stored in prev array.

# program to partition a Set 
# into Two Subsets of Equal Sum
# using space optimised
def equalPartition(arr):
    # Calculate sum of the elements in array
    arrSum = sum(arr)
    # If sum is odd, there cannot be two 
    # subsets with equal sum
    if arrSum % 2 != 0:
        return False

    arrSum = arrSum // 2

    n = len(arr)
    prev = [False] * (arrSum + 1)
    curr = [False] * (arrSum + 1)

    # Mark prev[0] = true as it is true
    # to make sum = 0 using 0 elements
    prev[0] = True

    # Fill the subset table in
    # bottom-up manner
    for i in range(1, n + 1):
        for j in range(arrSum + 1):
            if j < arr[i - 1]:
                curr[j] = prev[j]
            else:
                curr[j] = (prev[j] or prev[j - arr[i - 1]])

        prev = curr.copy()

    return prev[arrSum]

if __name__ == "__main__":
    arr = [1, 5, 11, 5]
    if equalPartition(arr):
        print("True")
    else:
        print("False")
