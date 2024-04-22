import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    # Initialize the sums of the diagonals
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0

    # Calculate the sums of both diagonals
    n = len(arr)  # Since the matrix is square, the number of rows is equal to the number of columns
    for i in range(n):
        primary_diagonal_sum += arr[i][i]  # Summing elements from the top-left to bottom-right
        secondary_diagonal_sum += arr[i][n - 1 - i]  # Summing elements from the top-right to bottom-left

    # Calculate and return the absolute difference between the two diagonal sums
    return abs(primary_diagonal_sum - secondary_diagonal_sum)

if __name__ == '__main__':
    import os
    import sys

    # Assuming 'OUTPUT_PATH' environment variable is set and points to a valid file path
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())  # Read the size of the matrix
    arr = []

    # Read the matrix
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    # Calculate the diagonal difference
    result = diagonalDifference(arr)

    # Write the result to the output file
    fptr.write(str(result) + '\n')
    fptr.close()
