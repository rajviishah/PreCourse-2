# Time Complexity : O(logn)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No





# Python code to implement iterative Binary
# Search. 

# It returns location of x in given array arr  
# if present, else returns -1 
def binarySearch(arr, l, r, x):

    # write your code here
    while l<= r:
        mid = int((l + r) / 2)
        # if x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1

        # if x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1

        else:
            return mid
    return -1


# Test array
arr = [2, 3, 4, 10, 40]
x = 10

# Function call 
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")