a = [4, 6, 1, 2, 8]

def sort(a):
    return sorted(a)



def my_func(b, c):

    for num in a:
        if num == c:
            return True
    return False



if __name__ == '__main__':

    b = sort(a)
    print(b)
    print(my_func(b, 1))
    print(my_func(b, 9))



