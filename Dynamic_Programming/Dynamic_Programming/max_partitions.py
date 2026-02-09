# Given a string s consisting of lowercase English letters, 
# partition s into the maximum number of substrings such that 
# no two substrings share a common character. Return the total number of such substrings.

# Function to find the maximum number of substrings
# such that there is no common character between them
def maxPartitions(s):
    # Arrays to store first and last occurrence of each character
    first = [-1] * 26
    last = [-1] * 26
    # Find the first and last occurrence of each character
    for i in range(len(s)):
        if first[ord(s[i]) - ord('a')] == -1:
            first[ord(s[i]) - ord('a')] = i
        last[ord(s[i]) - ord('a')] = i
    count = 0
    end = 0
    # Iterate through the string to find partitions
    for i in range(len(s)):
        # Expand interval
        end = max(end, last[ord(s[i]) - ord('a')])

        # When we reach the end of a partition
        if i == end:
            
            # New partition formed
            count += 1  
    return count

if __name__ == "__main__":
    s = "acbbcc"
    print(maxPartitions(s))