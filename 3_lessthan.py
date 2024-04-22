def main():

    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = []

    for i in a:
        if i < 5:
            b.append(i)
    
    print(b)
 
    b = [i for i in a if i < 5]

    num = int(input("Provide number "))
    c = [i for i in a if i < num]

    print(c)



    


if __name__ ==  "__main__":
    main()