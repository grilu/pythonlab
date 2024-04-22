import os

a = "Testzslsafosadnvjnsadvjnsfvjn"

try:
    with open('test.txt', 'w') as nf:
        nf.write(a)
    print(f"File 'test.txt' has been written in the directory: {os.getcwd()}")
except Exception as e:
    print(f"An error occurred: {e}")
