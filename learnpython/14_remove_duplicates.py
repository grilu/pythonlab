def getList():
    a =  [1, 2, 3, 4, 2, 3, 4, 7, 8, 9]
    return a

def main():
    nl = getList()
    b = list(set(nl))
    return b

if __name__ == '__main__':
    print(main())