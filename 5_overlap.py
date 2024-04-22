def main():

    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    c = []

# Iterate through the first list
    for item in a:
        if item in b and item not in c:
            c.append(item)
    

# Print the result
    print(c)


if __name__ == "__main__":
    main()