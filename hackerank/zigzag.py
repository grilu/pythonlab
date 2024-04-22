def findZigZagSequence(a, n):
    a.sort()
    mid = (n - 1) // 2  # Use (n - 1) // 2 to correctly find the middle index for zero-based indexing
    # Swap the middle element with the last element
    a[mid], a[n-1] = a[n-1], a[mid]

    # Start from the next to middle index up to the second to last element
    st = mid + 1
    ed = n - 2  # Adjust to avoid swapping the last element which is already set

    # Swap elements to create the zigzag from the middle to the second to last element
    while st <= ed:
        a[st], a[ed] = a[ed], a[st]
        st += 1
        ed -= 1  # Decrease ed to converge towards the middle

    # Print the array in a single line
    print(" ".join(map(str, a)))

# Handling multiple test cases
test_cases = int(input())
for _ in range(test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)
