Lexicographically permuatition
#Step by Step explanation

1. Find the "dip":
Scan from right to left.
Find the first element that is smaller than its neighbor to the right.
This is where we can make a “small increase.”

2. Find the element to swap with:
Scan from the right again.
Find the smallest element bigger than the dip.

3. Swap them:
Swap the dip with the element found in step 2.
Reverse the right part:
Reverse all elements to the right of the dip index.
This ensures the next permutation is just the next greater one.

i=n-2 is to find the dip
n-2 is second last element 
We start from second last element because we are going to compare each element with the one to its right.

if i>=o
to find the number greater than arr[i]

reverse arr[ i+1:] is to reverse (##splicing)