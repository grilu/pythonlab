def oddNumbers(l, r):
    # Write your code here
    
    for a in range(l, r+1):
        if a%2 == 1:
            print(a)
    
    return 

if __name__ == '__main__':
    
    l = int(input("Provide number l: "))
    r = int(input("Provide number r: "))
    
    print(oddNumbers(l, r))