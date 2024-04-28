"""
 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
 """

s1 = "---"
s2 = "|"

a = int(input("provide number of rows: "))


len = a
count = 0
for i in range(len):
    count += 1
    print((" " + s1) * a)
    print((s2 + "   ") * (a + 1))
    if count == a:
        print((" " + s1) * a)



