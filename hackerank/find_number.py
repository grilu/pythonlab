def findNumber(arr, k):
    # Check if 'k' is in the list 'arr'
    if k in arr:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    # Example usage:
    # Read input from the user or define it directly
    arr = list(map(int, input("Enter the elements of the array separated by space: ").split()))
    k = int(input("Enter the number to find: "))
    
    # Call the findNumber function and print the result
    result = findNumber(arr, k)
    print(result)
