#Leap year
year = int(input("Enter the year in 4 digits: "))
if (year%400 == 0) or (year%4 == 0 and year%100!=0):
    print("It is a leap year")
else:
    print("Not a leap year")