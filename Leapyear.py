year=int(input("enter the year : "))
if year%4==0 or year%400==0:
    print("this is a leap year ")
else:
    print("this is not a leap year")