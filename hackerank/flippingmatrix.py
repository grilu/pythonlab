def flippingMatrix(matrix):
    n = len(matrix) // 2
    total_max_sum = 0
    
    for i in range(n):
        for j in range(n):
            # Calculate positions and consider potential values after flipping
            top_left = matrix[i][j]
            bottom_left = matrix[2 * n - 1 - i][j]
            top_right = matrix[i][2 * n - 1 - j]
            bottom_right = matrix[2 * n - 1 - i][2 * n - 1 - j]
            
            # Maximum value that can be flipped into the top-left quadrant at (i, j)
            max_value = max(top_left, bottom_left, top_right, bottom_right)
            
            # Summing up the maximum values for the top-left quadrant
            total_max_sum += max_value
    
    return total_max_sum

# Integration with automated testing or manual input
if __name__ == '__main__':
    # Prepare file output if necessary (used in environments like HackerRank)
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # Read the size of the matrix from input
    q = int(input().strip())  # Number of queries or matrices
    
    results = []
    for _ in range(q):
        matrix = []
        n = int(input().strip()) * 2  # Each matrix is 2n x 2n, read n and double it
        
        for __ in range(n):
            row = list(map(int, input().rstrip().split()))
            matrix.append(row)
        
        # Append result of the flippingMatrix function call for the current matrix
        result = flippingMatrix(matrix)
        results.append(result)
    
    # Write results to output and then close the file pointer
    for result in results:
        fptr.write(str(result) + '\n')
    
    fptr.close()
