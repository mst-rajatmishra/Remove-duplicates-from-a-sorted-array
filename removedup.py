def removeDuplicates(arr):
    if not arr:
        return 0

    # Pointer for the position of the next unique element
    j = 0
    
    # Traverse the array with the second pointer
    for i in range(1, len(arr)):
        # If the current element is different from the last unique element
        if arr[i] != arr[j]:
            j += 1
            arr[j] = arr[i]
    
    # Return the length of the array with unique elements
    return j + 1

# Example usage
a = [1, 1, 2, 3, 3, 4, 4, 4, 4, 4, 4, 5, 6, 6, 7, 7, 8]
new_length = removeDuplicates(a)

print("Length of array with unique elements:", new_length)
print("Array with unique elements:", a[:new_length])
