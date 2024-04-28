import os


with open('prime.txt', 'r') as prime:
    a = prime.readlines()

with open('happy.txt', 'r') as happy:
    b = happy.readlines()

my_list = []

q = []
for i in a:
    for y in b:
        if int(i) == int(y):
            e = i.strip()
            my_list.append(int(e))

print(my_list)