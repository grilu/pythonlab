def getstr():
    str =  (input("Enter a sentence: "))
    return str

def main():
    a = getstr()

    b = a.split(" ")

    print(b[::-1])


if __name__ == '__main__':
    main()