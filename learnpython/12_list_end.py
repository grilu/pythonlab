def getalist():
    #a = [5, 10, 15, 20, 25]
    a = list(input("Enter a list:"))
    return a

def newlist(nl):
    b = []
    b.append(nl[0])
    b.append(nl[-1])
    return b

def main():
    nl = getalist()
    b = newlist(nl)
    print(b)




if __name__ == "__main__":
    main()