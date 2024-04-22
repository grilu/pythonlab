import datetime

age = int(input("What is your age: "))
#name = input("What is your name: ")

a = 100

yth = 100 - age

timea = datetime.date.today()

current_year = int(timea.year)

years = current_year + yth


print(years)
