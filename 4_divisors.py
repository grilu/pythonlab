
def main():
    
    num = int(input("What number? "))
    a = []
    for i in range(1, num+1):
        if num % i == 0:
            a.append(i)

    print(a)


if __name__ == "__main__":
    main()